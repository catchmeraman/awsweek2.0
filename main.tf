# AWS Amplify Unicorn Website Infrastructure
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

# Amplify App
resource "aws_amplify_app" "unicorn_website" {
  name       = var.app_name
  repository = var.github_repository

  # Build settings
  build_spec = <<-EOT
    version: 1
    frontend:
      phases:
        preBuild:
          commands:
            - npm ci
        build:
          commands:
            - npm run build
      artifacts:
        baseDirectory: dist
        files:
          - '**/*'
      cache:
        paths:
          - node_modules/**/*
  EOT

  # Environment variables
  environment_variables = {
    AMPLIFY_DIFF_DEPLOY = "false"
    AMPLIFY_MONOREPO_APP_ROOT = "."
  }

  # Enable auto branch creation
  enable_auto_branch_creation = true
  enable_branch_auto_build    = true
  enable_branch_auto_deletion = true

  tags = {
    Name        = var.app_name
    Environment = var.environment
  }
}

# Main branch
resource "aws_amplify_branch" "main" {
  app_id      = aws_amplify_app.unicorn_website.id
  branch_name = "main"

  framework = "Web"
  stage     = "PRODUCTION"

  enable_auto_build = true

  tags = {
    Name        = "${var.app_name}-main"
    Environment = var.environment
  }
}

# Custom domain (optional)
resource "aws_amplify_domain_association" "custom_domain" {
  count       = var.custom_domain != "" ? 1 : 0
  app_id      = aws_amplify_app.unicorn_website.id
  domain_name = var.custom_domain

  # Subdomain configuration
  sub_domain {
    branch_name = aws_amplify_branch.main.branch_name
    prefix      = ""
  }

  # Wait for DNS propagation
  wait_for_verification = true
}

# Route 53 hosted zone (if managing DNS)
resource "aws_route53_zone" "main" {
  count = var.manage_dns ? 1 : 0
  name  = var.custom_domain

  tags = {
    Name        = var.custom_domain
    Environment = var.environment
  }
}

# SSL Certificate
resource "aws_acm_certificate" "ssl_cert" {
  count           = var.custom_domain != "" ? 1 : 0
  domain_name     = var.custom_domain
  validation_method = "DNS"

  subject_alternative_names = [
    "*.${var.custom_domain}"
  ]

  lifecycle {
    create_before_destroy = true
  }

  tags = {
    Name        = var.custom_domain
    Environment = var.environment
  }
}

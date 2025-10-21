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
  name = var.app_name

  # Build settings for static website
  build_spec = <<-EOT
    version: 1
    frontend:
      phases:
        build:
          commands:
            - mkdir -p dist
            - cp index.html reports.html dist/
            - cp amplify-unicorn-architecture.png dist/
      artifacts:
        baseDirectory: dist
        files:
          - '**/*'
  EOT

  # Platform
  platform = "WEB"

  tags = {
    Name        = var.app_name
    Environment = var.environment
    Project     = "unicorn-website"
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

  # Subdomain configuration for awsweek2.cloudopsinsights.com
  sub_domain {
    branch_name = aws_amplify_branch.main.branch_name
    prefix      = "awsweek2"
  }

  # Wait for DNS propagation
  wait_for_verification = false
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

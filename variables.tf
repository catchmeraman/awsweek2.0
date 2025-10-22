variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "app_name" {
  description = "Name of the Amplify application"
  type        = string
  default     = "unicorn-website"
}

variable "github_repository" {
  description = "GitHub repository URL"
  type        = string
  default     = "https://github.com/catchmeraman/awsweek2.0"
}

variable "custom_domain" {
  description = "Custom domain name"
  type        = string
  default     = "cloudopsinsights.com"
}

variable "subdomain_prefix" {
  description = "Subdomain prefix for the custom domain"
  type        = string
  default     = "awsweek2"
}

variable "manage_dns" {
  description = "Whether to manage DNS with Route 53"
  type        = bool
  default     = false
}

variable "environment" {
  description = "Environment name"
  type        = string
  default     = "production"
}

output "amplify_app_id" {
  description = "Amplify App ID"
  value       = aws_amplify_app.unicorn_website.id
}

output "amplify_app_arn" {
  description = "Amplify App ARN"
  value       = aws_amplify_app.unicorn_website.arn
}

output "default_domain" {
  description = "Default Amplify domain"
  value       = "https://${aws_amplify_branch.main.branch_name}.${aws_amplify_app.unicorn_website.default_domain}"
}

output "custom_domain_url" {
  description = "Custom domain URL"
  value       = var.custom_domain != "" ? "https://awsweek2.${var.custom_domain}" : null
}

output "amplify_console_url" {
  description = "Amplify Console URL"
  value       = "https://console.aws.amazon.com/amplify/home?region=${var.aws_region}#/${aws_amplify_app.unicorn_website.id}"
}

output "dns_records" {
  description = "DNS records needed for custom domain"
  value = var.custom_domain != "" ? {
    certificate_validation = "Add CNAME record from Amplify console for SSL validation"
    subdomain_cname = "awsweek2 CNAME [CloudFront domain from Amplify console]"
  } : null
}

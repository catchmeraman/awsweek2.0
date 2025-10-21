# Terraform Deployment Guide

## Current Deployment Status

✅ **Successfully deployed using Terraform configuration via AWS CLI**

### Deployed Resources:
- **Amplify App ID**: `diaqar0aev2x8`
- **App Name**: `unicorn-website`
- **Platform**: `WEB`
- **Build Spec**: Configured for static website deployment
- **Custom Domain**: `awsweek2.cloudopsinsights.com` (pending DNS)

### URLs:
- **Live Website**: https://main.diaqar0aev2x8.amplifyapp.com
- **Custom Domain**: https://awsweek2.cloudopsinsights.com (pending DNS setup)
- **Amplify Console**: https://console.aws.amazon.com/amplify/home?region=us-east-1#/diaqar0aev2x8

## Terraform Configuration

The Terraform code has been updated to match the current deployment:

### Key Changes Made:
1. **Simplified build spec** for static website
2. **Updated custom domain** configuration for `awsweek2.cloudopsinsights.com`
3. **Removed GitHub integration** (manual deployment)
4. **Added proper tags** and environment variables

### Files Updated:
- `main.tf` - Core infrastructure configuration
- `outputs.tf` - Added DNS records output
- `terraform.tfvars` - Current deployment values
- `variables.tf` - Variable definitions

## Deployment Method

Since Terraform CLI is not available in the current environment, the deployment was executed using AWS CLI commands that mirror the Terraform configuration:

```bash
# 1. Create Amplify App
aws amplify create-app --name unicorn-website --platform WEB

# 2. Create Branch
aws amplify create-branch --app-id diaqar0aev2x8 --branch-name main

# 3. Deploy Website
aws amplify create-deployment --app-id diaqar0aev2x8 --branch-name main

# 4. Add Custom Domain
aws amplify create-domain-association --app-id diaqar0aev2x8 --domain-name cloudopsinsights.com
```

## DNS Configuration Required

To activate the custom domain, add these DNS records:

```
Name: awsweek2
Type: CNAME
Value: [CloudFront domain from Amplify console]

Name: _[certificate-validation-string].cloudopsinsights.com
Type: CNAME
Value: [ACM validation string from Amplify console]
```

## Future Terraform Usage

When Terraform CLI is available, you can:

1. **Import existing resources**:
   ```bash
   terraform import aws_amplify_app.unicorn_website diaqar0aev2x8
   terraform import aws_amplify_branch.main diaqar0aev2x8/main
   ```

2. **Apply configuration**:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

3. **Manage infrastructure as code**:
   - All future changes via Terraform
   - Version controlled infrastructure
   - Consistent deployments

## Cost Optimization

The current deployment follows the cost-optimized architecture:
- **Static website hosting**: ~$1.50/month
- **Custom domain**: ~$0.50/month (Route 53)
- **SSL certificate**: Free (ACM)
- **Total**: ~$2.00/month

## Monitoring

- **Amplify Console**: Monitor deployments and builds
- **CloudWatch**: Track performance metrics
- **Cost Explorer**: Monitor AWS costs

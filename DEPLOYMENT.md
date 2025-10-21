# 🚀 Manual Deployment Guide

## Quick Deploy to AWS Amplify

### Option 1: AWS Amplify Console (Recommended)

1. **Go to AWS Amplify Console**
   - Open [AWS Amplify Console](https://console.aws.amazon.com/amplify/)
   - Click "New app" → "Host web app"

2. **Connect GitHub Repository**
   - Select "GitHub" as source
   - Authorize AWS Amplify to access your GitHub
   - Select repository: `awsweek2.0`
   - Select branch: `main`

3. **Configure Build Settings**
   ```yaml
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
   ```

4. **Deploy**
   - Click "Save and deploy"
   - Wait for build to complete (~2-3 minutes)
   - Access your website at the provided URL

### Option 2: AWS CLI

```bash
# Run the deployment script
./deploy.sh
```

### Option 3: Terraform (Advanced)

```bash
# Initialize and apply Terraform
terraform init
terraform plan
terraform apply
```

## 🌐 Access Your Website

After deployment, your website will be available at:
- **Default Amplify URL**: `https://main.d[app-id].amplifyapp.com`
- **Custom Domain**: `cloudopsinsights.com` (if configured)

## 📊 What's Included

- **Main Website**: Beautiful unicorn-themed homepage
- **Reports Page**: Complete project documentation and cost analysis
- **Architecture Diagram**: Visual representation of the AWS infrastructure
- **Source Code**: All Terraform and website files
- **Cost Analysis**: Detailed monthly cost breakdown

## 💰 Expected Costs

- **Monthly Cost**: ~$2.00
- **Free Tier**: First 12 months mostly free
- **Components**: Amplify hosting + Route 53 (if using custom domain)

## 🔧 Customization

1. **Update Content**: Edit `index.html` and `reports.html`
2. **Modify Styling**: Update CSS in the `<style>` sections
3. **Add Pages**: Create new HTML files and link them
4. **Update Infrastructure**: Modify `main.tf` for additional AWS resources

## 📈 Monitoring

- **Amplify Console**: Monitor builds and deployments
- **CloudWatch**: Track performance metrics
- **Cost Explorer**: Monitor AWS costs

## 🆘 Troubleshooting

- **Build Fails**: Check build logs in Amplify console
- **Domain Issues**: Verify DNS settings and SSL certificate
- **Cost Concerns**: Monitor usage in AWS Cost Explorer

---

🦄 **Happy Deploying!** Your unicorn website will be live in minutes!

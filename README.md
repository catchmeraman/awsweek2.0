# AWS Amplify Unicorn Website

A simple, beautiful unicorn-themed website deployed on AWS Amplify with Terraform infrastructure as code.

## 🦄 Live Demo

- **Default Amplify URL**: Will be generated after deployment
- **Custom Domain**: cloudopsinsights.com (configured in Terraform)

## 🏗️ Architecture

![Architecture Diagram](amplify-unicorn-architecture.png)

### Components:
- **AWS Amplify**: Static website hosting with CI/CD
- **CloudFront**: Global CDN for fast content delivery
- **Route 53**: DNS management for custom domain
- **ACM**: Free SSL certificate
- **GitHub**: Source code repository with automated deployments

## 💰 Cost Analysis

**Estimated Monthly Cost: $2.00**

- **AWS Amplify**: $1.50/month (10GB data transfer, 5 builds)
- **Route 53**: $0.50/month (hosted zone)
- **ACM Certificate**: $0.00/month (free for AWS services)

**Free Tier Benefits:**
- First 12 months: 1,000 build minutes free
- First 12 months: 15GB data transfer free

See detailed cost analysis in `amplify-cost-analysis.md`

## 🚀 Deployment

### Prerequisites
- AWS CLI configured
- Terraform >= 1.0 installed
- GitHub repository access

### Quick Deploy

1. **Clone the repository**:
   ```bash
   git clone https://github.com/catchmeraman/awsweek2.0.git
   cd awsweek2.0
   ```

2. **Initialize Terraform**:
   ```bash
   terraform init
   ```

3. **Review and modify variables** (optional):
   ```bash
   # Edit variables.tf for custom settings
   vim variables.tf
   ```

4. **Deploy infrastructure**:
   ```bash
   terraform plan
   terraform apply
   ```

5. **Access your website**:
   - Check Terraform outputs for URLs
   - Default Amplify URL will be available immediately
   - Custom domain may take 24-48 hours for DNS propagation

### Manual Amplify Setup (Alternative)

If you prefer to set up Amplify manually:

1. Go to AWS Amplify Console
2. Connect your GitHub repository
3. Configure build settings (use the build spec in `main.tf`)
4. Deploy!

## 🛠️ Customization

### Website Content
- Edit `index.html` to customize the website
- Modify CSS styles in the `<style>` section
- Add more pages by creating additional HTML files

### Infrastructure
- Update `variables.tf` for different configurations
- Modify `main.tf` for additional AWS resources
- Adjust build settings in the Amplify app configuration

## 📁 Project Structure

```
awsweek2.0/
├── main.tf                     # Terraform infrastructure
├── variables.tf                # Configuration variables
├── outputs.tf                  # Terraform outputs
├── index.html                  # Main website file
├── package.json                # Build configuration
├── amplify-cost-analysis.md    # Detailed cost analysis
├── amplify-unicorn-architecture.png  # Architecture diagram
└── README.md                   # This file
```

## 🔧 Build Process

The website uses a simple build process:
1. **Pre-build**: Install dependencies (if any)
2. **Build**: Copy files to `dist/` directory
3. **Deploy**: Amplify serves files from `dist/`

Build specification is defined in the Terraform configuration.

## 🌟 Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Fast Loading**: Optimized for performance
- **Secure**: HTTPS by default with free SSL certificate
- **Scalable**: Auto-scaling CDN handles traffic spikes
- **CI/CD**: Automatic deployments on git push

## 📊 Monitoring

- **Amplify Console**: Monitor builds and deployments
- **CloudWatch**: Track performance metrics
- **Cost Explorer**: Monitor AWS costs

## 🔒 Security

- HTTPS enforced by default
- CloudFront provides DDoS protection
- No server-side components reduce attack surface
- Static files only - no database or backend vulnerabilities

## 🎯 Cost Optimization Tips

1. **Use Free Tier**: Take advantage of 12-month free tier
2. **Optimize Assets**: Compress images and minify CSS/JS
3. **Monitor Usage**: Set up billing alerts
4. **Cache Strategy**: Leverage CloudFront caching
5. **Build Efficiency**: Minimize build frequency and duration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

- **AWS Documentation**: [Amplify Hosting Guide](https://docs.aws.amazon.com/amplify/)
- **Terraform Documentation**: [AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/)
- **Issues**: Report bugs or request features via GitHub Issues

---

Built with ❤️ for CloudOps Insights | Powered by AWS Amplify

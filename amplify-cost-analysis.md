# AWS Amplify Unicorn Website Cost Analysis Estimate Report

## Service Overview

AWS Amplify Unicorn Website is a fully managed, serverless service that allows you to This project uses multiple AWS services.. This service follows a pay-as-you-go pricing model, making it cost-effective for various workloads.

## Pricing Model

This cost analysis estimate is based on the following pricing model:
- **ON DEMAND** pricing (pay-as-you-go) unless otherwise specified
- Standard service configurations without reserved capacity or savings plans
- No caching or optimization techniques applied

## Assumptions

- Static website with moderate traffic (10,000 visitors/month)
- 5 builds per month (1 build per week)
- 1GB of build artifacts storage
- 10GB data transfer per month
- US East (N. Virginia) region
- Using custom domain with Route 53
- Free ACM SSL certificate

## Limitations and Exclusions

- Advanced Amplify features (server-side rendering)
- WAF protection ($15/month)
- Additional data transfer beyond 10GB
- Premium support costs
- Development and maintenance time

## Cost Breakdown

### Unit Pricing Details

| Service | Resource Type | Unit | Price | Free Tier |
|---------|--------------|------|-------|------------|
| AWS Amplify Hosting | Data Transfer | GB served | $0.15 | First 12 months: 1,000 build minutes and 15GB data transfer free |
| AWS Amplify Hosting | Build Minutes | build minute | $0.01 | First 12 months: 1,000 build minutes and 15GB data transfer free |
| AWS Amplify Hosting | Storage | GB stored | $0.023 | First 12 months: 1,000 build minutes and 15GB data transfer free |
| Route 53 (Optional) | Hosted Zone | hosted zone per month | $0.50 | No free tier for Route 53 hosted zones |
| ACM Certificate | Certificate | 1 unit | $0.00 for public certificates | Free SSL certificates for AWS services |

### Cost Calculation

| Service | Usage | Calculation | Monthly Cost |
|---------|-------|-------------|-------------|
| AWS Amplify Hosting | Static website with 10,000 monthly visitors (Data Transfer: 10 GB/month, Build Minutes: 5 minutes/month, Storage: 1 GB) | ($0.15 × 10 GB) + ($0.01 × 5 min) + ($0.023 × 1 GB) = $1.50 + $0.05 + $0.023 = $1.57 | $1.50 |
| Route 53 (Optional) | Hosted zone for custom domain (Hosted Zones: 1 hosted zone) | $0.50 × 1 hosted zone = $0.50 | $0.50 |
| ACM Certificate | SSL certificate for custom domain (Certificates: 1 SSL certificate) | $0.00 - Free for AWS services | $0.00 |
| **Total** | **All services** | **Sum of all calculations** | **$2.00/month** |

### Free Tier

Free tier information by service:
- **AWS Amplify Hosting**: First 12 months: 1,000 build minutes and 15GB data transfer free
- **Route 53 (Optional)**: No free tier for Route 53 hosted zones
- **ACM Certificate**: Free SSL certificates for AWS services

## Cost Scaling with Usage

The following table illustrates how cost estimates scale with different usage levels:

| Service | Low Usage | Medium Usage | High Usage |
|---------|-----------|--------------|------------|
| AWS Amplify Hosting | $0/month | $1/month | $3/month |
| Route 53 (Optional) | $0/month | $0/month | $1/month |
| ACM Certificate | Varies | Varies | Varies |

### Key Cost Factors

- **AWS Amplify Hosting**: Static website with 10,000 monthly visitors
- **Route 53 (Optional)**: Hosted zone for custom domain
- **ACM Certificate**: SSL certificate for custom domain

## Projected Costs Over Time

The following projections show estimated monthly costs over a 12-month period based on different growth patterns:

Base monthly cost calculation:

| Service | Monthly Cost |
|---------|-------------|
| AWS Amplify Hosting | $1.50 |
| Route 53 (Optional) | $0.50 |
| **Total Monthly Cost** | **$2** |

| Growth Pattern | Month 1 | Month 3 | Month 6 | Month 12 |
|---------------|---------|---------|---------|----------|
| Steady | $2/mo | $2/mo | $2/mo | $2/mo |
| Moderate | $2/mo | $2/mo | $2/mo | $3/mo |
| Rapid | $2/mo | $2/mo | $3/mo | $5/mo |

* Steady: No monthly growth (1.0x)
* Moderate: 5% monthly growth (1.05x)
* Rapid: 10% monthly growth (1.1x)

## Detailed Cost Analysis

### Pricing Model

ON DEMAND


### Exclusions

- Advanced Amplify features (server-side rendering)
- WAF protection ($15/month)
- Additional data transfer beyond 10GB
- Premium support costs
- Development and maintenance time

### Recommendations

#### Immediate Actions

- Use Amplify free tier for first 12 months
- Optimize images and assets to reduce data transfer
- Implement caching strategies to reduce build frequency
- Monitor usage with CloudWatch to avoid unexpected costs
#### Best Practices

- Set up billing alerts for cost monitoring
- Use CloudFront caching to reduce data transfer costs
- Implement CI/CD best practices to minimize build times
- Consider using S3 + CloudFront for pure static sites if costs become significant



## Cost Optimization Recommendations

### Immediate Actions

- Use Amplify free tier for first 12 months
- Optimize images and assets to reduce data transfer
- Implement caching strategies to reduce build frequency

### Best Practices

- Set up billing alerts for cost monitoring
- Use CloudFront caching to reduce data transfer costs
- Implement CI/CD best practices to minimize build times

## Conclusion

By following the recommendations in this report, you can optimize your AWS Amplify Unicorn Website costs while maintaining performance and reliability. Regular monitoring and adjustment of your usage patterns will help ensure cost efficiency as your workload evolves.

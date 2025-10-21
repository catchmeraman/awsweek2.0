#!/bin/bash

# AWS Amplify Unicorn Website Deployment Script

echo "🦄 Deploying Unicorn Website to AWS Amplify..."

# Check if AWS CLI is configured
if ! aws sts get-caller-identity > /dev/null 2>&1; then
    echo "❌ AWS CLI not configured. Please run 'aws configure' first."
    exit 1
fi

# Create Amplify app
echo "📱 Creating Amplify app..."
APP_ID=$(aws amplify create-app \
    --name "unicorn-website" \
    --platform WEB \
    --build-spec '{
        "version": 1,
        "frontend": {
            "phases": {
                "preBuild": {
                    "commands": ["echo \"No pre-build needed\""]
                },
                "build": {
                    "commands": [
                        "mkdir -p dist",
                        "cp index.html dist/"
                    ]
                }
            },
            "artifacts": {
                "baseDirectory": "dist",
                "files": ["**/*"]
            }
        }
    }' \
    --tags Environment=production,Project=unicorn-website \
    --query 'app.appId' \
    --output text)

if [ $? -eq 0 ]; then
    echo "✅ Amplify app created with ID: $APP_ID"
else
    echo "❌ Failed to create Amplify app"
    exit 1
fi

# Create main branch
echo "🌿 Creating main branch..."
aws amplify create-branch \
    --app-id $APP_ID \
    --branch-name main \
    --framework "Web" \
    --stage PRODUCTION \
    --enable-auto-build

# Get the default domain
DOMAIN=$(aws amplify get-app --app-id $APP_ID --query 'app.defaultDomain' --output text)

echo ""
echo "🎉 Deployment initiated successfully!"
echo "📱 App ID: $APP_ID"
echo "🌐 Default URL: https://main.$DOMAIN"
echo ""
echo "📋 Next steps:"
echo "1. Connect your GitHub repository in the Amplify console"
echo "2. Trigger a build to deploy your website"
echo "3. Access your website at the URL above"
echo ""
echo "🔗 Amplify Console: https://console.aws.amazon.com/amplify/home?region=us-east-1#/$APP_ID"

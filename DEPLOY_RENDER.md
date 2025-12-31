# Deploy to Render (Free)

## Quick Deploy Steps

1. **Sign up at Render**: https://render.com
2. **Connect GitHub**: Link your GitHub account
3. **Create Web Service**:
   - Choose "Build and deploy from a Git repository"
   - Select your repo
   - Render will auto-detect the Dockerfile
4. **Configure**:
   - Name: `visual-behavior-analysis`
   - Environment: `Docker`
   - Plan: `Free`
   - Auto-deploy: `Yes`

## Get Your API Key

Once deployed, your app will be at: `https://your-app-name.onrender.com`

Generate API key:
```bash
curl -X POST "https://your-app-name.onrender.com/api-key/generate" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-app-key"}'
```

## Free Limits
- 750 hours/month
- Sleeps after 15min inactivity
- Slower cold starts
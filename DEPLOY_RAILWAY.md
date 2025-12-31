# Deploy to Railway (Free)

## Quick Deploy Steps

1. **Sign up at Railway**: https://railway.app
2. **Connect GitHub**: Link your GitHub account
3. **Deploy from GitHub**:
   ```bash
   # Push your code to GitHub first
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```
4. **Create new project** on Railway dashboard
5. **Deploy from GitHub repo** - Railway will auto-detect your Dockerfile
6. **Get your API URL** from Railway dashboard (e.g., `https://your-app.railway.app`)

## Get Your API Key

Once deployed, visit your app URL and generate an API key:

```bash
# Generate API key via endpoint
curl -X POST "https://your-app.railway.app/api-key/generate" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-app-key"}'
```

Or visit: `https://your-app.railway.app/docs` and use the Swagger UI.

## Free Limits
- 500 execution hours/month
- $5 credit monthly
- Automatic sleep after 30min inactivity
# Deploy to Fly.io (Free)

## Quick Deploy Steps

1. **Install flyctl**: https://fly.io/docs/hands-on/install-flyctl/
2. **Sign up**: `flyctl auth signup`
3. **Deploy**:
   ```bash
   flyctl launch --no-deploy
   flyctl deploy
   ```

## Get Your API Key

Your app will be at: `https://visual-behavior-analysis.fly.dev`

Generate API key:
```bash
curl -X POST "https://visual-behavior-analysis.fly.dev/api-key/generate" \
  -H "Content-Type: application/json" \
  -d '{"name": "my-app-key"}'
```

## Free Limits
- 3 shared-cpu-1x VMs
- 160GB/month outbound data transfer
- Auto-suspend when idle
# 🚂 Railway Deployment Guide

Complete guide for deploying your Visual Behavior Analysis API on Railway.

## ✅ Pre-Deployment Checklist

- [x] Dockerfile fixed for Debian Trixie
- [x] All files ready
- [x] Railway configs created

---

## 🚀 Step-by-Step Railway Deployment

### Step 1: Push Fixed Code to GitHub

```powershell
cd "C:\Users\91947\Desktop\video analysis"

# Add the fixed Dockerfile
git add Dockerfile

# Commit the fix
git commit -m "Fix Dockerfile for Railway deployment - Debian Trixie compatibility"

# Push to GitHub
git push
```

---

### Step 2: Deploy on Railway

#### 2.1 Sign Up / Login

1. Go to: **https://railway.app**
2. Click **"Login"** or **"Start a New Project"**
3. Sign up with **GitHub** (recommended - one click)
4. Authorize Railway to access your GitHub

#### 2.2 Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. If prompted, authorize Railway to access your repositories
4. Select your repository: **video-analysis-api** (or your repo name)
5. Railway will automatically:
   - Detect the Dockerfile
   - Start building your container
   - Deploy your API

#### 2.3 Monitor Deployment

- Watch the build logs in Railway dashboard
- Build typically takes 3-5 minutes
- You'll see progress in real-time

---

### Step 3: Configure Your Service

#### 3.1 Get Your Domain

1. After deployment completes, click on your service
2. Go to **"Settings"** tab
3. Scroll to **"Domains"** section
4. Click **"Generate Domain"**
5. Your API will be available at: `https://your-app-name.up.railway.app`

#### 3.2 Environment Variables (Optional)

Railway automatically sets:
- `PORT` - Automatically configured
- `RAILWAY_ENVIRONMENT` - Set to "production"

You can add custom variables in **Settings → Variables** if needed.

---

### Step 4: Generate API Key

After deployment, you need to generate your API key.

#### Option A: Via Railway CLI (Recommended)

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Link to your project (run in project directory)
railway link

# Generate API key
railway run python api_keys.py
```

#### Option B: Via API Endpoint

```bash
# Replace with your Railway URL
curl -X POST "https://your-app-name.up.railway.app/api-key/generate" \
  -H "Content-Type: application/json" \
  -d '{"name": "production_key", "expires_days": null}'
```

#### Option C: Via Railway Shell

1. Go to your service in Railway dashboard
2. Click **"Deployments"** tab
3. Click on the latest deployment
4. Use the **"Shell"** feature
5. Run: `python api_keys.py`
6. Copy the generated API key

---

## ✅ Step 5: Test Your Deployment

### 5.1 Health Check

```bash
curl https://your-app-name.up.railway.app/health
```

Expected response:
```json
{
  "status": "healthy",
  "analyzer_ready": true,
  "timestamp": 1704067200.0
}
```

### 5.2 View API Documentation

Open in browser:
```
https://your-app-name.up.railway.app/docs
```

### 5.3 Test Analysis Endpoint

```bash
API_KEY="your_generated_api_key"
API_URL="https://your-app-name.up.railway.app"

curl -X POST "$API_URL/analyze/frame" \
  -H "X-API-Key: $API_KEY" \
  -F "file=@test_frame.jpg"
```

---

## 🔧 Railway-Specific Features

### Auto-Deploy

Railway automatically redeploys when you push to GitHub:
- Push to `main` branch → Auto-deploy
- No manual deployment needed

### Monitoring

- **Logs**: View real-time logs in Railway dashboard
- **Metrics**: CPU, Memory, Network usage
- **Deployments**: View deployment history

### Scaling

- Railway automatically scales based on traffic
- Free tier: Limited resources
- Paid plans: More resources available

---

## 🔑 Save Your Credentials

Create a file to save your Railway deployment info:

```
RAILWAY_DEPLOYMENT.txt
=====================
Service Name: your-app-name
API URL: https://your-app-name.up.railway.app
API Key: your_generated_api_key_here
Documentation: https://your-app-name.up.railway.app/docs
```

---

## 🆘 Troubleshooting

### Build Fails

1. **Check build logs** in Railway dashboard
2. **Verify Dockerfile** is correct
3. **Check requirements.txt** has all dependencies
4. **Ensure** all files are committed to GitHub

### API Not Responding

1. **Check service status** in Railway dashboard
2. **View logs** for errors
3. **Verify** health endpoint: `/health`
4. **Check** API key is correct

### Port Issues

Railway automatically sets `PORT` environment variable. Your Dockerfile should use:
```dockerfile
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
```

This is already configured! ✅

### Memory Issues

If you get out-of-memory errors:
1. Go to **Settings → Resources**
2. Increase memory allocation
3. Or upgrade to a paid plan

---

## 📊 Railway Dashboard Features

### View Logs
- Real-time logs
- Filter by deployment
- Search logs

### Metrics
- CPU usage
- Memory usage
- Network traffic
- Request count

### Settings
- Environment variables
- Domain configuration
- Resource limits
- Build settings

---

## 🔄 Updating Your Deployment

### Automatic Updates

1. Make changes to your code
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update API"
   git push
   ```
3. Railway automatically detects changes and redeploys

### Manual Redeploy

1. Go to Railway dashboard
2. Click on your service
3. Click **"Deployments"** tab
4. Click **"Redeploy"** on any deployment

---

## 💰 Railway Pricing

### Free Tier
- $5 credit/month
- 512MB RAM
- 1GB storage
- Good for testing

### Paid Plans
- Pay-as-you-go
- More resources
- Better performance
- No credit limits

---

## ✅ Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Project created on Railway
- [ ] Repository connected
- [ ] Build successful
- [ ] Domain generated
- [ ] API key generated
- [ ] Health check passing
- [ ] API tested
- [ ] Documentation accessible

---

## 🎉 Success!

Your API is now live on Railway! 🚂

**Your API URL**: `https://your-app-name.up.railway.app`

**Next Steps:**
1. Generate and save your API key
2. Test all endpoints
3. Integrate into your applications
4. Monitor usage in Railway dashboard

---

## 📞 Railway Support

- **Railway Docs**: https://docs.railway.app
- **Railway Discord**: https://discord.gg/railway
- **Railway Status**: https://status.railway.app

---

**Your Visual Behavior Analysis API is ready for production on Railway! 🚀**


# 🔧 Railway PORT Variable Fix

## ✅ Fixed Files

1. **start.sh** - Created startup script that properly handles PORT variable
2. **Dockerfile** - Updated to use the startup script
3. **railway.json** - Removed startCommand (uses Dockerfile CMD)
4. **railway.toml** - Removed startCommand (uses Dockerfile CMD)

## 🚨 Important: Check Railway Dashboard

If you're still getting the PORT error, Railway might have a **startCommand** set in the dashboard that's overriding the Dockerfile.

### Fix in Railway Dashboard:

1. Go to your Railway project
2. Click on your service
3. Go to **Settings** tab
4. Scroll to **"Deploy"** section
5. Look for **"Start Command"** field
6. **DELETE** or **CLEAR** any startCommand value
7. Leave it **EMPTY** (Railway will use Dockerfile CMD)
8. Save changes

The startCommand in the dashboard overrides the Dockerfile CMD, so it must be empty!

## 📤 Deploy the Fix

```powershell
cd "C:\Users\91947\Desktop\video analysis"

# Add new files
git add start.sh Dockerfile railway.json railway.toml

# Commit
git commit -m "Fix PORT variable handling with startup script"

# Push
git push
```

## ✅ How It Works Now

1. **start.sh** script reads PORT from environment
2. Defaults to 8000 if PORT not set
3. Properly expands the variable before passing to uvicorn
4. Railway automatically sets PORT environment variable

## 🧪 Test After Deployment

```bash
# Health check
curl https://your-app.up.railway.app/health

# Should return:
# {"status":"healthy","analyzer_ready":true,"timestamp":...}
```

## 🆘 Still Having Issues?

If the error persists:

1. **Check Railway Dashboard** - Remove any startCommand
2. **Check Logs** - View deployment logs in Railway
3. **Verify PORT is set** - Railway automatically sets it
4. **Redeploy** - Trigger a new deployment

The startup script approach is the most reliable way to handle PORT in Railway!


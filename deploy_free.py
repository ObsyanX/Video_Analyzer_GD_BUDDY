#!/usr/bin/env python3
"""
Free Deployment Helper for Visual Behavior Analysis API

Helps deploy to free platforms and get API keys.
"""

import subprocess
import sys
import json
import requests
import time
from pathlib import Path

def check_git_repo():
    """Check if we're in a git repository."""
    try:
        subprocess.run(["git", "status"], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError:
        return False

def setup_git_if_needed():
    """Initialize git repo if needed."""
    if not check_git_repo():
        print("Setting up git repository...")
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        print("✅ Git repository initialized")

def deploy_to_railway():
    """Deploy to Railway."""
    print("\n🚂 Deploying to Railway...")
    print("1. Go to https://railway.app")
    print("2. Sign up with GitHub")
    print("3. Create new project")
    print("4. Deploy from GitHub repo")
    print("5. Railway will auto-detect your Dockerfile")
    print("\nAfter deployment, your app will be at: https://your-app.railway.app")

def deploy_to_render():
    """Deploy to Render."""
    print("\n🎨 Deploying to Render...")
    print("1. Go to https://render.com")
    print("2. Sign up with GitHub")
    print("3. Create Web Service")
    print("4. Choose 'Build and deploy from Git repository'")
    print("5. Select your repo")
    print("6. Use these settings:")
    print("   - Environment: Docker")
    print("   - Plan: Free")
    print("\nAfter deployment, your app will be at: https://your-app.onrender.com")

def deploy_to_fly():
    """Deploy to Fly.io."""
    print("\n🪰 Deploying to Fly.io...")
    try:
        # Check if flyctl is installed
        subprocess.run(["flyctl", "version"], check=True, capture_output=True)
        
        print("flyctl detected. Deploying...")
        subprocess.run(["flyctl", "launch", "--no-deploy"], check=True)
        subprocess.run(["flyctl", "deploy"], check=True)
        print("✅ Deployed to Fly.io")
        
    except subprocess.CalledProcessError:
        print("flyctl not found. Install it first:")
        print("1. Visit: https://fly.io/docs/hands-on/install-flyctl/")
        print("2. Install flyctl")
        print("3. Run: flyctl auth signup")
        print("4. Run this script again")

def generate_api_key(base_url):
    """Generate API key from deployed app."""
    print(f"\n🔑 Generating API key from {base_url}...")
    
    try:
        # Wait for app to be ready
        print("Waiting for app to be ready...")
        for i in range(30):  # Wait up to 30 seconds
            try:
                response = requests.get(f"{base_url}/health", timeout=5)
                if response.status_code == 200:
                    break
            except:
                pass
            time.sleep(1)
            print(".", end="", flush=True)
        
        print("\nGenerating API key...")
        response = requests.post(
            f"{base_url}/api-key/generate",
            json={"name": "deployment-key"},
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            api_key = data.get("api_key")
            print(f"\n✅ API Key Generated: {api_key}")
            print(f"\n📋 Save this API key! Use it in your apps:")
            print(f"   X-API-Key: {api_key}")
            
            # Save to file
            with open("API_KEY.txt", "w") as f:
                f.write(f"API_KEY={api_key}\n")
                f.write(f"API_URL={base_url}\n")
            print(f"\n💾 API key saved to API_KEY.txt")
            
            return api_key
        else:
            print(f"❌ Failed to generate API key: {response.text}")
            
    except Exception as e:
        print(f"❌ Error generating API key: {e}")
        print(f"\n🔧 Manual steps:")
        print(f"1. Visit: {base_url}/docs")
        print(f"2. Use the /api-key/generate endpoint")
        print(f"3. Save the generated API key")
    
    return None

def test_api_key(base_url, api_key):
    """Test the generated API key."""
    print(f"\n🧪 Testing API key...")
    
    try:
        headers = {"X-API-Key": api_key}
        response = requests.get(f"{base_url}/api-key/info", headers=headers, timeout=10)
        
        if response.status_code == 200:
            print("✅ API key is working!")
            print(f"📊 API Documentation: {base_url}/docs")
            return True
        else:
            print(f"❌ API key test failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error testing API key: {e}")
    
    return False

def main():
    """Main deployment flow."""
    print("=" * 60)
    print("🚀 Visual Behavior Analysis API - Free Deployment")
    print("=" * 60)
    
    # Setup git if needed
    setup_git_if_needed()
    
    print("\nChoose deployment platform:")
    print("1. Railway (Recommended - Easy)")
    print("2. Render (Good alternative)")
    print("3. Fly.io (Developer friendly)")
    print("4. Show all deployment guides")
    
    choice = input("\nEnter choice (1-4): ").strip()
    
    if choice == "1":
        deploy_to_railway()
        print("\nAfter deployment, enter your app URL to generate API key:")
        url = input("App URL (e.g., https://your-app.railway.app): ").strip()
        if url:
            api_key = generate_api_key(url)
            if api_key:
                test_api_key(url, api_key)
    
    elif choice == "2":
        deploy_to_render()
        print("\nAfter deployment, enter your app URL to generate API key:")
        url = input("App URL (e.g., https://your-app.onrender.com): ").strip()
        if url:
            api_key = generate_api_key(url)
            if api_key:
                test_api_key(url, api_key)
    
    elif choice == "3":
        deploy_to_fly()
        # Fly.io has predictable URLs
        url = "https://visual-behavior-analysis.fly.dev"
        api_key = generate_api_key(url)
        if api_key:
            test_api_key(url, api_key)
    
    elif choice == "4":
        print("\n📚 Deployment guides created:")
        print("- DEPLOY_RAILWAY.md")
        print("- DEPLOY_RENDER.md") 
        print("- DEPLOY_FLY.md")
        print("\nChoose one platform and follow the guide!")
    
    else:
        print("Invalid choice. Run the script again.")
    
    print("\n" + "=" * 60)
    print("🎉 Deployment complete!")
    print("Use your API key in other applications with:")
    print("  Header: X-API-Key: your_api_key_here")
    print("=" * 60)

if __name__ == "__main__":
    main()
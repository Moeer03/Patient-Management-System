import subprocess
import time
import sys
import os

# Step 1: Start the FastAPI backend
backend = subprocess.Popen(
    [sys.executable, "-m", "uvicorn", "main:app", "--reload"],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print("🚀 Starting FastAPI backend...")
time.sleep(3)  # Wait a few seconds for backend to be ready

# Step 2: Start the Streamlit frontend
print("🎨 Launching Streamlit frontend...")
subprocess.run([sys.executable, "-m", "streamlit", "run", "frontend.py"])

# Step 3: When frontend closes, stop backend
print("🛑 Stopping backend...")
backend.terminate()

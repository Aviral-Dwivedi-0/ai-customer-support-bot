import requests
import time
import sys

# Wait a moment for server to start
time.sleep(2)

BASE_URL = "http://localhost:5000"

print("\n" + "="*60)
print("   🧪 Quick API Test")
print("="*60)

try:
    # Test 1: Health Check
    print("\n✅ Test 1: Health Check")
    response = requests.get(f"{BASE_URL}/health", timeout=5)
    print(f"   Response: {response.json()}")
    
    # Test 2: Simple FAQ Query
    print("\n✅ Test 2: FAQ Query")
    payload = {
        "session_id": "quick_test",
        "query": "Do you ship internationally?"
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload, timeout=10)
    print(f"   Query: {payload['query']}")
    print(f"   Response: {response.json()['response']}")
    
    print("\n" + "="*60)
    print("   ✅ API is working perfectly!")
    print("="*60 + "\n")
    
except requests.exceptions.ConnectionError:
    print("\n❌ Error: Could not connect to server.")
    print("   Make sure Flask is running on http://localhost:5000")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)

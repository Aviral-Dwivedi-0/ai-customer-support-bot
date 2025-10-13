import requests
import json

BASE_URL = "http://localhost:5000"

def test_health():
    """Test health endpoint"""
    print("\n🧪 Testing Health Endpoint...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
    assert response.status_code == 200
    print("   ✅ Health check passed")

def test_faq_match():
    """Test FAQ matching"""
    print("\n🧪 Testing FAQ Match...")
    payload = {
        "session_id": "test_faq",
        "query": "Do you ship internationally?"
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"   Status: {response.status_code}")
    print(f"   Query: {payload['query']}")
    print(f"   Response: {response.json()['response']}")
    assert response.status_code == 200
    assert "50 countries" in response.json()['response'] or "internationally" in response.json()['response'].lower()
    print("   ✅ FAQ match test passed")

def test_context_memory():
    """Test conversational context"""
    print("\n🧪 Testing Context Memory...")
    session_id = "test_context"
    
    # First query
    payload1 = {"session_id": session_id, "query": "What is your return policy?"}
    response1 = requests.post(f"{BASE_URL}/chat", json=payload1)
    print(f"   Query 1: {payload1['query']}")
    print(f"   Response 1: {response1.json()['response']}")
    
    # Follow-up query
    payload2 = {"session_id": session_id, "query": "How many days do I have?"}
    response2 = requests.post(f"{BASE_URL}/chat", json=payload2)
    print(f"   Query 2: {payload2['query']}")
    print(f"   Response 2: {response2.json()['response']}")
    
    response_text = response2.json()['response'].lower()
    assert "30" in response_text or "thirty" in response_text
    print("   ✅ Context memory test passed")

def test_escalation():
    """Test escalation trigger"""
    print("\n🧪 Testing Escalation...")
    payload = {
        "session_id": "test_escalation",
        "query": "What is the weather today?"
    }
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(f"   Query: {payload['query']}")
    print(f"   Response: {response.json()['response']}")
    assert "escalate" in response.json()['response'].lower()
    print("   ✅ Escalation test passed")

def test_escalation_endpoint():
    """Test escalation summary endpoint"""
    print("\n🧪 Testing Escalation Summary Endpoint...")
    # First create some conversation
    payload1 = {
        "session_id": "test_escalation_summary",
        "query": "What is your return policy?"
    }
    requests.post(f"{BASE_URL}/chat", json=payload1)
    
    # Now get the summary
    payload2 = {"session_id": "test_escalation_summary"}
    response = requests.post(f"{BASE_URL}/escalate", json=payload2)
    print(f"   Status: {response.status_code}")
    print(f"   Summary: {response.json()['summary']}")
    assert response.status_code == 200
    print("   ✅ Escalation summary test passed")

if __name__ == "__main__":
    print("="*60)
    print("   🚀 Running AI Customer Support Bot API Tests")
    print("="*60)
    
    try:
        test_health()
        test_faq_match()
        test_context_memory()
        test_escalation()
        test_escalation_endpoint()
        
        print("\n" + "="*60)
        print("   ✅ ALL TESTS PASSED!")
        print("="*60 + "\n")
    except AssertionError as e:
        print(f"\n   ❌ Test failed: {e}")
    except requests.exceptions.ConnectionError:
        print("\n   ❌ Error: Could not connect to server. Make sure Flask is running on http://localhost:5000")
    except Exception as e:
        print(f"\n   ❌ Unexpected error: {e}")

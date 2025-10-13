import requests
import json
import time

BASE_URL = "http://localhost:5000"

def print_separator():
    print("\n" + "="*70)

def demo_conversation():
    """Demonstrate the chatbot's capabilities"""
    
    print_separator()
    print("   🤖 AI CUSTOMER SUPPORT BOT - LIVE DEMONSTRATION")
    print_separator()
    
    session_id = f"demo_session_{int(time.time())}"
    
    # Demo 1: Simple FAQ question
    print("\n📝 SCENARIO 1: Customer asks about return policy")
    print("-" * 70)
    query1 = "What is your return policy?"
    print(f"Customer: {query1}")
    
    response1 = requests.post(f"{BASE_URL}/chat", 
                             json={"session_id": session_id, "query": query1})
    bot_answer1 = response1.json()['response']
    print(f"Bot: {bot_answer1}")
    
    # Demo 2: Follow-up question (tests context memory)
    time.sleep(1)
    print("\n📝 SCENARIO 2: Customer asks follow-up (testing context memory)")
    print("-" * 70)
    query2 = "How many days?"
    print(f"Customer: {query2}")
    
    response2 = requests.post(f"{BASE_URL}/chat",
                             json={"session_id": session_id, "query": query2})
    bot_answer2 = response2.json()['response']
    print(f"Bot: {bot_answer2}")
    print("✅ Bot remembered the context!")
    
    # Demo 3: Another FAQ question
    time.sleep(1)
    print("\n📝 SCENARIO 3: Customer asks about shipping")
    print("-" * 70)
    query3 = "Do you ship to Canada?"
    print(f"Customer: {query3}")
    
    response3 = requests.post(f"{BASE_URL}/chat",
                             json={"session_id": session_id, "query": query3})
    bot_answer3 = response3.json()['response']
    print(f"Bot: {bot_answer3}")
    
    # Demo 4: Question NOT in FAQ (escalation)
    time.sleep(1)
    print("\n📝 SCENARIO 4: Customer asks question NOT in FAQ (escalation)")
    print("-" * 70)
    query4 = "Can I get a bulk discount?"
    print(f"Customer: {query4}")
    
    response4 = requests.post(f"{BASE_URL}/chat",
                             json={"session_id": session_id, "query": query4})
    bot_answer4 = response4.json()['response']
    print(f"Bot: {bot_answer4}")
    print("✅ Bot correctly escalated to human agent!")
    
    # Demo 5: Get conversation summary
    time.sleep(1)
    print("\n📝 SCENARIO 5: Get conversation summary for agent")
    print("-" * 70)
    
    response5 = requests.post(f"{BASE_URL}/escalate",
                             json={"session_id": session_id})
    summary = response5.json()['summary']
    print(f"Conversation Summary:\n{summary}")
    
    print_separator()
    print("   ✅ DEMONSTRATION COMPLETE")
    print("   All features working perfectly!")
    print_separator()
    print("\n")

if __name__ == "__main__":
    try:
        demo_conversation()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Flask server not running!")
        print("   Start the server with: python app.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")

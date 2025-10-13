import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

# Test 1: Simple test
print("Test 1: Simple API test")
response = model.generate_content("Say 'Hello, API is working!' if you can read this.")
print(f"Response: {response.text}\n")

# Test 2: FAQ test
print("Test 2: FAQ test")
faq_content = """Q: Do you ship internationally?
A: Yes, we ship to over 50 countries worldwide. Shipping costs vary by location."""

prompt = f"""Answer this question based on the FAQ:

FAQ:
{faq_content}

Question: Do you ship internationally?

Answer:"""

response = model.generate_content(prompt)
print(f"Response: {response.text}\n")

print("✅ Gemini API is working correctly!")

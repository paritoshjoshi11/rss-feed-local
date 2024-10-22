from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()
genai.configure(api_key=os.environ.get('API_KEY'))
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Give summary on spongebob square pant in 100 words")
print(response.text)
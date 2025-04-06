import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('models/gemini-1.5-flash-002')


response = model.generate_content(contents="Who won Wimbledon this year?",
                                  tools='google_search_retrieval')

print(response)
from google import genai
from google.genai import types


client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents="Who won the US open this year?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(
            google_search=types.GoogleSearchRetrieval
        )]
    )
)
print(response)
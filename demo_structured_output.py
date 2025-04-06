import os
from google import genai
from pydantic import BaseModel

# Define your structured output model
class EclipseEvent(BaseModel):
    date: str
    time_utc: str
    description: str
    visibility: str
    countries_where_is_visible: list

# Configure the API key
client = genai.Client(api_key=os.environ["API_KEY"])
# Define the content generation config
config = {
    "response_mime_type":"application/json",
    "response_schema":EclipseEvent,
}

# Generate structured content
response = client.models.generate_content(
     model='gemini-1.5-flash-002',
    contents="When is the next total solar eclipse in the United States?",
    tools='google_search_retrieval',
    config=config
)

# Structured response: raw JSON and parsed object
print(response.text)  # Raw JSON string
eclipse_info: EclipseEvent = response.parsed  # Parsed Pydantic object
print(eclipse_info)

# Grounding metadata if available
print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)

from google import genai
from google.genai.types import HttpOptions

import logging
from google.cloud import logging as gcp_logging

# For Qwiklabs internal logging
gcp_logging_client = gcp_logging.Client()
gcp_logging_client.setup_logging()

client = genai.Client(
    vertexai=True,
    project='qwiklabs-gcp-00-1c386a9205fa',
    location='us-east4',
    http_options=HttpOptions(api_version="v1")
)

chat = client.chats.create(model="gemini-2.0-flash-001")
response_text = ""

for chunk in chat.send_message_stream("What are all the colors in a rainbow?"):
    print(chunk.text, end="")
    response_text += chunk.text


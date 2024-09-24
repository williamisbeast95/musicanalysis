import http.client
import json
import base64
import os
# Path to your local MP3 file
file_path = 'audio/song.mp3'

# Read the MP3 file and encode it to base64
with open(file_path, "rb") as mp3_file:
    file_content = mp3_file.read()
    encoded_file = base64.b64encode(file_content).decode("utf-8")

# Create the payload with the base64-encoded MP3 file
payload = json.dumps({
    "file": encoded_file
})

headers = {
    'x-rapidapi-key': os.getenv('Sonoteller_API_KEY'),
    'x-rapidapi-host': "sonoteller-ai1.p.rapidapi.com",
    'Content-Type': "application/json"
}

# Send the request
conn = http.client.HTTPSConnection("sonoteller-ai1.p.rapidapi.com")
conn.request("POST", "/music", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

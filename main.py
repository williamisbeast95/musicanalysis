import http.client
import os
# Path to your local MP3 file
file_path = 'audio/song.mp3'
# Read the MP3 file and encode it to base64
with open(file_path, "rb") as mp3_file:
    file_content = mp3_file.read()

headers = {
    'x-rapidapi-key': os.getenv('Sonoteller_API_KEY'),
    'x-rapidapi-host': "sonoteller-ai1.p.rapidapi.com",
    'Content-Type': "application/json"
}

# Send the request
conn = http.client.HTTPSConnection("sonoteller-ai1.p.rapidapi.com")
conn.request("POST", "/music", body=file_content, headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

import http.client

conn = http.client.HTTPSConnection("sonoteller-ai1.p.rapidapi.com")

payload = "{\"file\":\"https://storage.googleapis.com/musikame-files/thefatrat-mayday-feat-laura-brehm-lyriclyrics-videocopyright-free-music.mp3\"}"

headers = {
    'x-rapidapi-key': "4e1056282cmsh8fdbd0c320caf21p1e1b3cjsnd7c046c55c93",
    'x-rapidapi-host': "sonoteller-ai1.p.rapidapi.com",
    'Content-Type': "application/json"
}

conn.request("POST", "/music", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
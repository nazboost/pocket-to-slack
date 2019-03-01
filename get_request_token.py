import requests
import settings

payload = {
    'consumer_key': settings.consumer_key,
    'redirect_uri': 'http://localhost:80'
}
r = requests.post('https://getpocket.com/v3/oauth/request', data=payload)

print(r.content)

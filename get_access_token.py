import requests
import settings

payload = {
    'consumer_key': settings.consumer_key,
    'code': settings.code
}
r = requests.post('https://getpocket.com/v3/oauth/authorize', data=payload)

print(r.content)

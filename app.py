import os
import random
import sys

import requests
import slackweb

import settings

os.environ['CONSUMER_KEY'] = settings.consumer_key
os.environ['ACCESS_TOKEN'] = settings.access_token
os.environ['WEBHOOK_URL'] = settings.webhook_url


def main():
    payload = {
        'consumer_key': os.environ['CONSUMER_KEY'],
        'access_token': os.environ['ACCESS_TOKEN'],
        'state': 'unread'
    }
    r = requests.post('https://getpocket.com/v3/get', data=payload)
    articles = r.json()['list']

    words_per_min = 600

    article_id = random.choice(list(articles.keys()))

    read_time = int(articles[article_id]['word_count']) / words_per_min
    if read_time < 1:
        read_time_text = str(round(read_time * 60, 1)) + ' sec to read'
    else:
        read_time_text = str(round(read_time, 1)) + ' min to read'

    slack = slackweb.Slack(url=os.environ['WEBHOOK_URL'])

    text = articles[article_id]['resolved_title'] + \
        '\n' + articles[article_id]['resolved_url'] + \
        '\n' + read_time_text

    slack.notify(text=text)


if __name__ == "__main__":
    main()

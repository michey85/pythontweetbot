import tweepy as tp
import time

# credential to login to twitter api | from https://developer.twitter.com/en/apps/
consumer_key = 'your key'
consumer_secret = 'your secret'
access_token = 'your token'
access_secret = 'your secret'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

# Список статусов
# В папке с программой создайте папку с изображениями img
tweets = [
    ['./img/имя_картинки.jpg', 'текст твита'],
    ['./img/имя_картинки.jpg', 'текст твита']
]

for tweet in tweets:
    image = tweet[0]
    text = tweet[1]
    api.update_with_media(image, text) # docs https://tweepy.readthedocs.io/en/v3.5.0/api.html#timeline-methods
    time.sleep(300) # 300сек = 5 минут; укажите желаемый интервал публикации


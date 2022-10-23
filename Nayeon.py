from operator import length_hint
import random
import tweepy
import time
import os
import shutil


API_KEY = ""
API_SECRET = ""

ACCESS_TOKEN = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

api = tweepy.API(auth)

global CANT_IMG

CANT_IMG = len(os.listdir("images/"))


def job(text):
    api.update_status(text)


def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])


a = os.listdir("images/")

tam = len(a)

if tam == 0: 
    a = os.listdir("img/")

vec = random.sample(a, CANT_IMG)


while True:
    for imgPosted in vec:

        texto = "#나연 #NAYEON #TWICE 🐰"

        archivo = "images/%s" % (imgPosted)

        # schedule.every(3).hours.do(upload_media, texto, archivo)

        upload_media(texto, archivo)

        if tam == 0: 
            shutil.move ("img/%s"%imgPosted, "images/%s"%imgPosted)
        else:
            shutil.move ("images/%s"%imgPosted, "img/%s"%imgPosted)

        time.sleep(7200)

    vec = random.sample(a, CANT_IMG)

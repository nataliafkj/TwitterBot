from operator import length_hint
import random
import tweepy
import time
import os
import shutil


API_KEY = "evvoknpZeD135PfQMD2VxgreY"
API_SECRET = "9yqHqGTenljCMSScpoQxfbu10jH88PDkaV9xNH0Sp9dN0pBhvz"

ACCESS_TOKEN = "1499523277613453312-PW53aADzzNpv4ZgbGDsjYMhXsuZcLA"
ACCESS_SECRET = "rTOSln8T6De68reJr7dwCx91x7hjfCYhhCZOIIjo7JysH"

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
    a = os.listdir("alreadyPosted/")

vec = random.sample(a, CANT_IMG)


while True:
    for imgPosted in vec:

        texto = "#나연 #NAYEON #TWICE 🐰"

        archivo = "images/%s" % (imgPosted)

        # schedule.every(3).hours.do(upload_media, texto, archivo)

        upload_media(texto, archivo)

        if tam == 0: 
            shutil.move ("alreadyPosted/%s"%imgPosted, "images/%s"%imgPosted)
        else:
            shutil.move ("images/%s"%imgPosted, "alreadyPosted/%s"%imgPosted)

        time.sleep(18000)

    vec = random.sample(a, CANT_IMG)

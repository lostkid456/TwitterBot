#Twitter
#Author:Johnathan Zhao

import tweepy
import sys, os, json, webbrowser

CONFIG_FILE="my_twitterbot.config"

def create_twitter_api():

    f=open(CONFIG_FILE,"r")
    config=json.load(f)
    consumer_key=config["consumer_key"]
    consumer_secret=config["consumer_secret"]
    access_token=config["access_token"]
    access_token_secret=config["access_token_secret"]


    auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

    return api
    

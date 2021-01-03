# My Twitter Bot 
# Johnathan Zhao 

import Twit
import time
import sys
import Generate
import time 

delay=3600*6



def main():
    api=Twit.create_twitter_api()
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
    while(True):
        tweet=Generate.generate_random_statement()
        print(tweet)
        status=api.update_status(tweet)
        print(status.id)
        time.sleep(delay)

main()

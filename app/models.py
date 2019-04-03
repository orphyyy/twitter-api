from datetime import datetime
from app.repositories import TweetRepository

class Tweet():
    def __init__(self, text):
        self.text = text
        #print(f'tweet text = {text}')
        self.created_at = datetime.now()
        self.id = None

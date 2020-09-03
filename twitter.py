import tweepy
import time
import re
from PIL import Image, ImageDraw, ImageFont
import sys
import textwrap


auth = tweepy.OAuthHandler('D2mYfaNGanCyTfpCCtTCIYWyq', '0w1nUpY2XdtdWRgsmLRzFxANL4jmQ5oMH6rmXRalWuU7q5rIe2')
auth.set_access_token('2739173399-yUiUwi6qIbcJBBBUb1XT1dvkhRfS38CRA8WCMgg', '871hOAbaW6nnpaGaTeRT6N9Sq0SZeZkwqSmYLobBAnjLJ')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
search = 'teste9832403'
numeroDeTweets = 10



for tweet in tweepy.Cursor(api.search, search).items(numeroDeTweets):
    try:
        tweetid = tweet.in_reply_to_status_id
        status = api.get_status(tweetid)
        text = status.text
        head, sep, tail = text.partition('https://t.co/')
        W, H = (1200,720)
        img = Image.open("mem.png")
        draw = ImageDraw.Draw(img)
        w, h = draw.textsize(head)
        myFont = ImageFont.truetype("arial.ttf", 32)
        draw.text(((W-w)/2, 200), head, fill="black", font=myFont)
        img.save('meme.png')

        api.update_with_media( 'meme.png', 
                status="@"+ tweet.user.screen_name + " ",
                in_reply_to_status_id=tweet.id,
            )
        print(head)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

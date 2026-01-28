import praw
import os
from dotenv import load_dotenv
import random
import time

load_dotenv() 

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD")
)

try:
    print(f"✅ Logged in as: {reddit.user.me()}")
except Exception as e:
    print(f"⚠️ Login failed: {e}")
    exit()

subreddit_name = "test" 
subreddit = reddit.subreddit(subreddit_name)

normal_replies = [
    "Thank you for sharing this.",
    "Interesting post!",
    "I found this helpful.",
    "Great content, thanks for posting!"
]

print(f"⏳ Monitoring new posts in r/{subreddit_name}...")

for submission in subreddit.stream.submissions(skip_existing=True):
    try:
        print(f"💬 New post found: {submission.title}")
        submission.reply(random.choice(normal_replies)) # Reply with a random message
        print(f"💖 Successfully replied to: {submission.title}")
        time.sleep(15) # To avoid rate limiting
    except Exception as e:
        print(f"⚠️ Could not reply: {e}")
        time.sleep(60) # Wait before retrying in case of an error
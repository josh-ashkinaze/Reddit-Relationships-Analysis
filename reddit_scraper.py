import praw 
import pandas as pd
from sys import argv


CLIENT_ID = 'CLIENT_ID'
SECRET_ID = 'SECRET_ID'
PW = 'PW'
USERNAME = 'USERNAME'
reddit = praw.Reddit(
                     client_id=CLIENT_ID,
                     client_secret= SECRET_ID,
                     password=PW,
                     user_agent='testscript by /u/giddygithub,
                     username=USERNAME
                     )

def retrieve_data(subreddit, nposts):
  """ Main function -- 
  Downloads post data for top n posts of a subreddit """
  sample = generate_posts(subreddit, nposts)
  post_data = parse_submissions(sample)
  df = pd.DataFrame(post_data)
  df.to_csv("{}{}.csv".format(subreddit, nposts))

def generate_posts(subreddit, nposts):
  """ Gathers a sample of top nposts """
  sample = []
  sub = reddit.subreddit(subreddit)
  for submission in sub.top(limit=n):
    update_list(sample, submission)
    print("Sample size: {}".format(len(sample)))
  return sample


def parse_submissions(submissions): 
  """ Parse a set of reddit posts """
  all_post_data = []
  for post in submissions:
    all_post_data.append(get_post_data(post))
    print("Parsed post {} of {}".format(len(all_post_data), len(submissions)))
  return all_post_data

def get_post_data(post):
  """ 
  Parse a reddit post.
  Return a dict of info containing:

  - title
  - flair
  - post_id 
  - self_txt
  - score
  - timestamp 
  - author
  - upvote_ratio
  """
  post_info = { 
    "title": post.title,
    "flair": post.link_flair_text ,
    "post_id": post.id,
    'self_txt' : post.selftext,
    "score": post.score,
    "timestamp":post.created_utc,
    "author":post.author, 
    "upvote_ratio": post.upvote_ratio,
  }
  return post_info
  

def update_list(input_list, candinate):
  """ Add candinate to list if not already in list """
  if candinate in input_list:
    pass
  else: 
    input_list.append(candinate)
  return input_list
  
def main():  
  sub, nposts = "relationships", 1000
  retrieve_data(sub, nposts)

if __name__ == "__main__":
  try:
    sub = sys.argv[0]
    n = sys.argv[1] 
    retrieve_data(sub, n)
  except: 
    print("Please enter the subreddit followed by desired number of posts to scrape.")


  main()

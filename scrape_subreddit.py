import praw 
import pandas as pd
import warnings


CLIENT_ID = 'SECRET'
SECRET_ID = 'SECRET'
PW = 'SECRET'
USERNAME = 'SECRET'
reddit = praw.Reddit(
                     client_id=CLIENT_ID,
                     client_secret= SECRET_ID,
                     password=PW,
                     user_agent='testscript by /u/fakebot3',
                     username=USERNAME
                     )


# Get a random sample of posts
def generate_posts(subreddit, nposts):
  sample = []
  sub = reddit.subreddit(subreddit)
  for i in range(nposts):
    random_post = sub.random()
    if random_post not in sample:
      sample.append(random_post)
  return sample

# Parse a set of posts
def parse_submissions(submissions): 
  submission_count = 0
  all_post_data = []
  for post in submissions:
    all_post_data.append(get_post_data(post))
    submission_count+=1
    print("POST {} OF MAX: {}".format(submission_count, len(submissions)))
  return all_post_data



# Returns info about a post 
def get_post_data(post):
  post_info = {
    "title": post.title,
    "flair": post.link_flair_text	,
    "post_id": post.id,
    'self_txt' : post.selftext,
    "score": post.score,
    "upvote_ratio": post.upvote_ratio,
    "num_comments" : post.num_comments,
  }
  return post_info

# Check if item in list and update list if not
def already_added(added_list, item):
  if item in added_list:
    return True
  else: 
    added_list.append(item)
    return False

# Execute functions to download sample data as csv
def download_sample(subredit, nposts):
   sample = generate_posts(subreddit, nposts)
   post_data = parse_submissions(sample)
   df = pd.DataFrame(post_data)
   df.to_csv("rship.csv")

def main():
  """Download data for a sample of n posts from a subreddit 

  Keyword args:
  subreddit -- subreddit to scrape
  nposts -- posts to scrape 

  Will return a CSV with the following info:
  1. title
  2. flair
  3. post_id
  4. self text
  5. score
  6. upvote ratio 
  7. number of comments 
  """
  download_sample('relationship_advice', 1000)
  
if __name__ == "__main__":
  main()

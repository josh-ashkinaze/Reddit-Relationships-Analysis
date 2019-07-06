# An analysis of the Reddit "Relationships" subreddit

I use exploratory data analysis and machine learning to understand what Redditors talk about when they talk about love. 

Look at the .ipynb file for my analysis. 

List of files in repo:
* reddit_scraper.py scrapes top N reddit posts of subreddit S
  * It returns the following information for each post that is scraped:
	 * author 
	 * flair 
	 * post_id 
	 * score 
	 * self_txt 
	 * timestamp 
	 * title 
	 * upvote_ratio
 * relationships_data.csv
 	*  888 top posts from r/relationships
 * reddit_analysis.ipynb
 	* A python notebook containing analysis of the data

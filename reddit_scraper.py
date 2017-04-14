import praw

PRAW_INIT_FILE_NAME = 'praw_init.txt'

class PrawInitData:
	def __init__(self, client_id, client_secret, user_agent, username, password):
		self.client_id = client_id
		self.client_secret = client_secret
		self.user_agent = user_agent
		self.username = username
		self.password = password

def make_praw_instance(init_data):
	return praw.Reddit(client_id=init_data.client_id, client_secret=init_data.client_secret, password=init_data.password,
					   user_agent=init_data.user_agent, username=init_data.username)

def get_titles_from_praw(reddit, n):
	return [submission.title for submission in reddit.subreddit('worldnews').hot(limit=n)]

def initialize_praw(file_name):
	file = open(file_name)
	file_line_list = tuple([line.rstrip() for line in file])
	return PrawInitData(*file_line_list)


def get_hot_post_titles(n):
	praw_init_fields = initialize_praw(PRAW_INIT_FILE_NAME)
	reddit = make_praw_instance(praw_init_fields)
	return get_titles_from_praw(reddit, n)
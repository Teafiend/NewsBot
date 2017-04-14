import praw

PRAW_INIT_FILE_NAME = 'praw_init.txt'

class PrawInitData:
	def __init__(self, client_id, client_secret, password, user_agent, username):
		self.client_id = client_id
		self.client_secret = client_secret
		self.password = password
		self.user_agent = user_agent
		self.username = username

def make_praw_instance(init_data):
	return praw.Reddit(init_data.client_id, init_data.client_secret, init_data.password,
						 init_data.user_agent, init_data.username)

def get_titles_from_praw(reddit, n):
	return [submission.title for submission in reddit.front.hot(limit=n)]

def initialize_praw(file_name):
	file = open(file_name)
	file_line_list = tuple([line for line in file])
	return PrawInitData(*file_line_list)


def get_hot_post_titles(n):
	praw_init_fields = initialize_praw(PRAW_INIT_FILE_NAME)
	reddit = make_praw_instance(praw_init_fields)
	return get_titles_from_praw(reddit, n)
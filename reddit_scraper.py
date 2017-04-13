import praw

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

def get_hot_post_titles(reddit, n):
	return [submission.title for submission in reddit.front.hot(limit=n)]

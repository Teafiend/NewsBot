import feedparser
import urllib.parse

GOOGLE_ROOT_URL = "https://news.google.com/?"

def encode_url(query):
	param_dict = {"output": "rss", "q": query}
	return GOOGLE_ROOT_URL + urllib.parse.urlencode(param_dict)

def parse_query(url):
	return feedparser.parse(url)

def get_titles_and_links(query):
	url = encode_url(query)
	parsed_data = parse_query(url)
	return_list = []
	for entry in parsed_data['entries']:
		return_list.append((entry['title'], entry['link'].split('url=')[-1]))
	return return_list

import reddit_scraper as rs
import google_feed_parser as gfp

NUMBER_OF_POSTS

"""
1. Scrape reddit for top n posts.
2. For each of these posts, get the associated RSS feed and parse it.
3. Collect the top-m headlines/links from the RSS feeds and aggregate them.
4. Construct an email containing these n*m headlines/links.
"""

def aggregate_headlines_and_links(number_of_posts, pairs_per_post):
	titles = rs.get_hot_post_titles(number_of_posts)
	all_pairs = []
	for t in titles:
		headlines = gfp.get_titles_and_links(t)
		if pairs_per_post >= len(headlines):
			all_pairs.extend(headlines)
		else:
			all_pairs.extend(headlines[:pairs_per_post])
	return all_pairs

def print_headlines_and_links(number_of_posts, pairs_per_post):
	pairs = aggregate_headlines_and_links(number_of_posts, pairs_per_post)
	for p in pairs:
		print("{} ({:20}...)".format(p[0], p[1]))
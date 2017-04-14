import reddit_scraper as rs
import google_feed_parser as gfp

NUMBER_OF_POSTS = 5
PAIRS_PER_POST  = 1

"""
1. Scrape reddit for top n posts.
2. For each of these posts, get the associated RSS feed and parse it.
3. Collect the top-m headlines/links from the RSS feeds and aggregate them.
4. Construct an email containing these n*m headlines/links.
"""

# TODO: Let user select their favorite news websites.
#       Can filter pairs with p[0].split('-')[-1]

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
		print("{} ({:.40}...)".format(p[0], p[1]))

if __name__ == "__main__":
	print_headlines_and_links(NUMBER_OF_POSTS, PAIRS_PER_POST)
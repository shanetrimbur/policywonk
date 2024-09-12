import feedparser

def fetch_rss_feed(url):
    feed = feedparser.parse(url)
    return [{'title': entry.title, 'link': entry.link} for entry in feed.entries]

if __name__ == "__main__":
    url = "https://rss.politicsnews.com/feed"  # Replace with actual political RSS feed URL
    entries = fetch_rss_feed(url)
    for entry in entries:
        print(f"Title: {entry['title']}, Link: {entry['link']}")

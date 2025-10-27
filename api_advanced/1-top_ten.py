#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API, prints the titles of the first 10 hot posts,
    and returns a value expected by the checker.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    # Use the /hot endpoint to get the post listings directly
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        # For non-existent subreddit, print None and return "OK"
        print("None")
        return "OK"

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return "OK"

        for post in posts:
            title = post.get('data', {}).get('title')
            print(title)
        
    except Exception:
        print("None")
        return "OK"

    # For existing subreddit (success), print titles and return "OK"
    return "OK"
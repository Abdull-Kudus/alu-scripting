#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            title = post.get('data', {}).get('title')
            print(title)
        
    except Exception:
        print("None")

    return
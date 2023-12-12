#!/usr/bin/python3
"""
number of subscribers for a given subreddit
"""

from requests import get


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    req = get(
          "https://www.reddit.com/r/{}/about.json".format(subreddit),
          headers={"User-Agent": "nerraou"},
                )
    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0

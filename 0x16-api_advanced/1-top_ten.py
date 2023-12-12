#!/usr/bin/python3
"""
 prints the titles of the first 10 hot posts listed for a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    res = get(
          "https://www.reddit.com/r/{}/hot.json".format(subreddit),
          headers={"User-Agent": "nerraou"},
          params={"limit": 10},
                )
    if res.status_code == 200:
        for data in res.json().get("data").get("children"):
            values = data.get("data")
            title = values.get("title")
            print(title)
    else:
        print(None)

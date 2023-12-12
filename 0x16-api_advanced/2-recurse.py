#!/usr/bin/python3
"""
Recurse it!
"""

from requests import get


def recurse(subreddit, hot_list=[], after=""):
    if subreddit is None or not isinstance(subreddit, str):
        return (None)
    res = get(
          "https://www.reddit.com/r/{}/hot.json".format(subreddit),
          headers={"User-Agent": "nerraou"},
          params={"after": after},
          allow_redirects=False
                )
    if res.status_code == 200:
        for data in res.json().get("data").get("children"):
            values = data.get("data")
            title = values.get("title")
            hot_list.append(title)
        after = res.json().get("data").get("after")
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return(None)

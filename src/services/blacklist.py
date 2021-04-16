import os
import pandas as pd
from urllib.parse import urlparse

import urllib.request
# import requests
# r = requests.get('https://www.google.com//https://www.bilibili.com') 
# print(r.history)

# response = urllib.request.urlopen('http://app.response.unity3d.com/e/er?utm_campaign=newnews_global_activation_motiva%3A%3A9184%3A%3ANT%20flow%20-%20email%2013%3A%3ASTO&utm_content=2020-01-global-beginner-PE-NT-13&utm_medium=email&utm_source=Eloqua&s=795651218&lid=8330&elqTrackId=e2c525849a8f4cf7858dddfe5b659e53&elq=c8fba62a064c4761ad71e06ae18e617a&elqaid=22711&elqat=1')
# print(response.geturl())

currentPath = os.getcwd();

good = pd.read_csv(os.getcwd() + "/src/assets/gooddomain.csv")
bad = pd.read_csv(os.getcwd() + "/src/assets/baddomain.csv")

# Test case, delete later:

# url = 'https://www.google.com/'
# domain = urlparse(url).netloc
# blacklist = []
# blacklist = bad.loc[bad.domain == domain]
# whitelist = []
# whitelist = good.loc[good.domain == domain]
# print(len(blacklist))
# print(len(whitelist))
# if len(blacklist) > 0:
#     print('the url is in the blacklist')
# else:
#     print('the url is not in the blacklist')
# if len(whitelist) > 0:
#     print('the url is in the whitelist')
# else:
#     print('the url is not in the whitelist')

def blacklist(url):
    domain = urlparse(url).netloc
    blacklist = []
    whitelist = []

    blacklist = bad.loc[bad.domain == domain]
    whitelist = good.loc[good.domain == domain]

    # return value
    # 0: whitelist, 1: blacklist, -1: nethier
    if len(blacklist) > 0:
        return 1;

    if len(whitelist) > 0:
        return 0;

    return -1;

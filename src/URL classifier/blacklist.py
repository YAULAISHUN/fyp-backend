import pandas as pd
from urllib.parse import urlparse
good = pd.read_csv('data/gooddomain.csv')
bad = pd.read_csv('data/baddomain.csv')
url = 'https://www.google.com/'
domain = urlparse(url).netloc
blacklist = []
blacklist = bad.loc[bad.domain == domain]
whitelist = []
whitelist = good.loc[good.domain == domain]
print(len(blacklist))
print(len(whitelist))
if len(blacklist) > 0:
    print('the url is in the blacklist')
else:
    print('the url is not in the blacklist')
if len(whitelist) > 0:
    print('the url is in the whitelist')
else:
    print('the url is not in the whitelist')
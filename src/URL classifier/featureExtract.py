import numpy as np
import pandas as pd
import re
import random
import joblib
import urllib
from features import *
import whois
df = pd.read_csv('urldata8.csv')
t=0
#df = df.loc[0:10, :]
def collectFeaturns(url):
    global t
    t+=1
    print(t)
    try:
        w = whois.whois(url)
        now = datetime.datetime.now()

        try:
            start = w.expiration_date
            expiration = (now - start[0]).days
        except:
            start = w.expiration_date
            expiration = (now - start).days
        try:
            start = w.updated_date
            update = -(now - start[0]).days
        except:
            start = w.updated_date
            update = -(now - start[0]).days
        return update, expiration
    except:
        return 0, 0
a = np.array([collectFeaturns(url) for url in df['url']])
print(a)
df['update'] = np.array([url[0] for url in a])
df['expire'] = np.array([url[1] for url in a])
df.to_csv('urldata9.csv')


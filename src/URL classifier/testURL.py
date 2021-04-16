import numpy as np
import pandas as pd
import re
import random
import joblib
import urllib
from features import *
prepare_pipeline = joblib.load('preditive model/vectorizer.pkl')
forest = joblib.load('preditive model/forest.pkl')
url = "http://www.hangsang.com"
data = {'url':[url],
        'shorten':[shortening_service(url)],
        'age':[whoisAge(url)],
        'response':[responseTime(url)],
        'alexa':[alexaRank(url)]}
print(data)
a = pd.DataFrame(data)
aa = prepare_pipeline.transform(a)
print(forest.predict(aa))

import numpy as np
import pandas as pd
import re
import random
import joblib
import urllib
from features import *
df = pd.read_csv('../urldata9.csv')
prepare_pipeline = joblib.load('finalvectorizer.pkl')
forest = joblib.load('finalforest.pkl')
X = df.loc[:, ['url', 'whois','shorten','age','response','alexa','update','expire']]
y = df.loc[:, 'result']
from sklearn.ensemble import RandomForestClassifier
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.ensemble import ExtraTreesClassifier
X_afterpipeline, y = make_classification(n_samples=45018, n_features=22, n_informative=5, n_redundant=5, random_state=1, n_classes=2)
forest = RandomForestClassifier(max_depth=3000, random_state=0, n_estimators=25, n_jobs=-1 )
forest.fit(X_afterpipeline, y)
importances = forest.feature_importances_
print(importances)
xlabel = ['length','domainLengh','pathlength','topdomain','#','num_path','num_subdoamin',
          'percent', 'at', 'euqal', 'letterNum', 'digitNUm', 'useIP', 'doubleslash','redirect',
          'shortenURL', 'SSL', 'age',' expire', 'update', 'response', 'ranking']
pyplot.bar(xlabel, importances)
pyplot.xticks(rotation=90)
#pyplot.xticks(range(X.shape[1]), importances)
pyplot.show()
import numpy as np
import pandas as pd
import re
import random
import joblib
import urllib
from features import *
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
df = pd.read_csv('data/urldata9.csv')
#good = df.loc[df['label'] == 'benign']
#bad = df.loc[df['label'] == 'malicious']
#print(good.shape)
#print(bad.shape)

X = df.loc[:, ['url', 'whois','shorten','age','response','alexa','update','expire']]
y = df.loc[:, 'result']
print(X)

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import FeatureUnion

count = CountVectorizer()
cc = changeContent()
prepare_pipeline = FeatureUnion([
    ('length', getURLength()),
    ('domainlength', getDomainLength()),
    ('pathlength', getPathLength()),
    ('topdomain', getFirstDomainLength()),
    ('hashtag', getHashTagNum()),
    ('slash', getSlashNum()),
    ('dot', getDotNum()),
    ('percent', getPercentNum()),
    ('at', getAtNum()),
    ('euqal', getEqualNum()),
    ('letterNum', getLetterNum()),
    ('digitNUm', getDigitNum()),
    ('useIP', getUseIP()),
    #('completewhois', compeleteWhois()),
    ('doubleslash', presenceDoubleSlash()),
    #('redirect', getRedirect()),
    ('shortenURL', getShorten()),
    ('SSL', getSSL_train()), #train the class to getSSL_train() when training model
    ('age', getAge()),
    #('expire', getExpire()),
    #('update', getUpdate()),
    ('response', getResponse()),
    ('ranking', getAlexa())
])

X_afterpipeline = prepare_pipeline.fit_transform(X[['url', 'shorten', 'age','response','alexa','update','expire']])
#print(X_afterpipeline.shape)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X_afterpipeline, y, test_size=0.2, random_state=42)
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
X_train = scalar.fit_transform (X_train)
X_test = scalar.fit_transform (X_test)
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1,max_iter=1000000)
lr.fit(X_train, y_train)
print(lr.score(X_test,y_test))

#from sklearn.ensemble import RandomForestClassifier
#forest = RandomForestClassifier(max_depth=10000, random_state=0, n_estimators=25, n_jobs=-1 )
#forest.fit(X_train, y_train)
#print(forest.score(X_test,y_test))

#from sklearn.svm import SVC
#svm =  SVC(probability=True, C=10)
#svm.fit(X_train, y_train)
#print(svm.score(X_test,y_test))


#joblib.dump(lr, "lr.pkl", protocol=2)
#joblib.dump(prepare_pipeline, "vectorizer.pkl", protocol=2)
#joblib.dump(svm, "svm.pkl", protocol=2)
#joblib.dump(forest, "forest.pkl", protocol=2)

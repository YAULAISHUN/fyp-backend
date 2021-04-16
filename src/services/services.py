import numpy as np
import re
from urllib.parse import urlparse
def getWordsFromURL(url):
    return re.compile(r'[\:/?=\-&.]+',re.UNICODE).split(url)

from sklearn.base import BaseEstimator, TransformerMixin

class getURLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([len(url) for url in X]).reshape(-1,1)

class getDomainLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([len(urlparse(url).netloc) for url in X]).reshape(-1,1)

class getPathLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([len(urlparse(url).path) for url in X]).reshape(-1,1)

class getSlashNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([url.count('/') for url in X]).reshape(-1,1)

class getDotNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([url.count('.') for url in X]).reshape(-1,1)

class getPercentNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([url.count('%') for url in X]).reshape(-1,1)


class getAtNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        return np.array([url.count('@') for url in X]).reshape(-1,1)

class changeContent(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X, y=None):
        print(1)
        X_return = []
        for url in X:
            words = getWordsFromURL(url)
            url2 = ' '.join(words)
            X_return.append(url2)
        return X_return
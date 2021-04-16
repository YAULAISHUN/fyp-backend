import re
from urllib.parse import urlparse
import numpy as np
import datetime
from tld import get_tld
import ipaddress
import socket
import time
import urllib
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request

def getWordsFromURL(url):
    return re.compile(r'[\:/?=\-&.]+', re.UNICODE).split(url)

def shortening_service(url):
    short = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      url)
    if short:
        return -1
    else:
        return 1

from sklearn.base import BaseEstimator, TransformerMixin


class getURLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        print('check lexical feature')
        return np.array([len(url) for url in X['url']]).reshape(-1, 1)


class getDomainLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([len(urlparse(url).netloc) for url in X['url']]).reshape(-1, 1)

def getTld(url):
    try:
        a = len(get_tld(url, fail_silently=True))
        return a
    except:
        return 0
class getFirstDomainLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([getTld(url) for url in X['url']]).reshape(-1, 1)

class getPathLength(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([len(urlparse(url).path) for url in X['url']]).reshape(-1, 1)


class changeContent(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        X_return = []
        for url in X:
            words = getWordsFromURL(url)
            url2 = ' '.join(words)
            X_return.append(url2)
        return X_return


class getHashTagNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        print('hashtag')
        tx = np.array([url.count('#') for url in X['url']]).reshape(-1, 1)
        return tx


class getPercentNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([urlparse(url).path.count('%') for url in X['url']]).reshape(-1, 1)


class getDotNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([urlparse(url).netloc.count('.') for url in X['url']]).reshape(-1, 1)


class getSlashNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([urlparse(url).path.count('/') for url in X['url']]).reshape(-1, 1)


class getAtNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([url.count('@') for url in X['url']]).reshape(-1, 1)


class getEqualNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([url.count('=') for url in X['url']]).reshape(-1, 1)

def digitNum(url):
    number = 0
    for i in url:
        if i.isnumeric():
            number+=1
    return number
def letterNum(url):
    number = 0
    for i in url:
        if i.isalpha():
            number += 1
    return number
class getDigitNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([digitNum(url) for url in X['url']]).reshape(-1, 1)
class getLetterNum(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([letterNum(url) for url in X['url']]).reshape(-1, 1)

def useIP(url):
    try:
        ipaddress.ip_address(url)
        return 1
    except:
        return 0
class getUseIP(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([useIP(url) for url in X['url']]).reshape(-1, 1)

def doubleSlash(url):
    u = urlparse(url).netloc + urlparse(url).path
    a = u.count('//')
    if a > 0:
        return 1
    else:
        return 0


class presenceDoubleSlash(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        print('check double slash')
        return np.array([doubleSlash(url) for url in X['url']]).reshape(-1, 1)

import whois
def completewhois(url):
    print('complete whois')
    try:
        w = whois.whois(url)
        print('success')
        return 1
    except:
        print('not success')
        return 0
def getWhois(x):
    if (x == 1):
        return 1
    else:
        return 0

def whoisAge(url):
    print('whois age')
    try:
        w = whois.whois(url)
        start = w.creation_date
        now = datetime.datetime.now()
        try:
            age = (now - start[0]).days
        except:
            age = (now - start).days
        return age
    except:
        return 0


class compeleteWhois(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        print('check complete whois')
        return np.array([getWhois(url) for url in X['whois']]).reshape(-1, 1)

class getShorten(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        print('check complete whois')
        return np.array([url for url in X['shorten']]).reshape(-1, 1)

import socket
import ssl
from urllib.parse import urlparse
def SSLstate(url):
    domain = urlparse(url).netloc
    hostname = domain
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                print(ssock.version())
                return 1
    except:
        return 0

class getSSL(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        tx = np.array([SSLstate(url) for url in X['url']]).reshape(-1, 1)
        return tx

class getAge(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([url for url in X['age']]).reshape(-1, 1)


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
socket.setdefaulttimeout(5)
def responseTime(url):
    global t
    print('response time')
    try:
        req = urllib.request.Request(url, headers=headers)
        start = time.perf_counter()
        webpage = urlopen(req).read()
        a = time.perf_counter() - start
        return a
    except:
        return 5

class getResponse(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        return np.array([url for url in X['response']]).reshape(-1, 1)


def alexaRank(url):
    try:
        rank_str = BeautifulSoup(urllib.request.urlopen("https://www.alexa.com/minisiteinfo/" + url),'html.parser').table.a.get_text()
        rank_int = int(rank_str.replace(',', ''))
        return rank_int
    except:
        return -1

class getAlexa(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X, y=None):
        return np.array([url for url in X['alexa']]).reshape(-1, 1)
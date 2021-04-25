import flask

import sys
sys.path.insert(1, './src/services/')

import joblib
import pandas as pd

from services import getURLength, getDomainLength, getDotNum, getPathLength, getPercentNum, getAtNum, getSlashNum, getURLength, getWordsFromURL, changeContent
from features import *
from blacklist import *

from flask_cors import CORS

import re

# app configuration
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False
CORS(app)

# load models
# decesionTreeModel = joblib.load('./src/models_old/decesionTree.pkl')
# logisticRegressionModel = joblib.load('./src/models_old/logisticRegression.pkl')
# randomForestModel = joblib.load('./src/models_old/randomForest.pkl')
# vectorizer = joblib.load('./src/models_old/vectorizer.pkl')

classifier = joblib.load('./src/models/classifier.pkl')
vectorizer = joblib.load('./src/models/vectorizer.pkl')

# avaliable models
listOfModels = [
    "Decesion Tree",
    "Logistic Regression",
    "Random Forest"
]

# / route
@app.route('/', methods=['GET'])
def home():
    return "<h1>FYP20054 Back-end</h1><p>Avaliable endpoints for this server: <ul><li><p>/classify (exmaple: <a href=\"localhost:5000/classify?url=www.google.com\">localhost:5000/classify?url=www.google.com</a>)</p></li></ul></p>"

# /classify route
@app.route('/classify', methods=['GET'])
def classify():
    url = flask.request.args.get('url')
    response = {
        # "url": url,
        # "predict": [
        #     {
        #         "model": None,
        #         "result": None,
        #         "explanation": None
        #     },
        #     {
        #         "model": None,
        #         "result": None,
        #         "explanation": None
        #     },
        #     {
        #         "model": None,
        #         "result": None,
        #         "explanation": None
        #     }
        # ]
        "url": url,
        "blacklist": {
            "result": None,
            "explanation": None
        },
        "predict": {
            "result": None,
            "explanation": None
        }
    }

    # transformedUrl = vectorizer.transform([url])
    # resultBydecesionTree = decesionTreeModel.predict(transformedUrl)
    # resultByLogisticRegression = logisticRegressionModel.predict(transformedUrl)
    # resultByRandomForest = randomForestModel.predict(transformedUrl)

    # results = [resultBydecesionTree[0], resultByLogisticRegression[0], resultByRandomForest[0]]
    # results = map(int, results)
    
    # for index, result in enumerate(results):
    #     response["predict"][index]["model"] = listOfModels[index]
    #     response["predict"][index]["result"] = result
    #     if result:
    #         response["predict"][index]["explanation"] = f"The {listOfModels[index]} model predicts the input URL is a malicious URL"
    #     else:
    #         response["predict"][index]["explanation"] = f"The {listOfModels[index]} model predicts the input URL is a benign URL"

    # validate url
    if not re.match('(?:http|ftp|https)://', url):
        url = 'http://{}'.format(url)

    # check blacklist
    isBlacklist = blacklist(url)

    response["blacklist"]["result"] = isBlacklist

    if isBlacklist == 0:
        response["blacklist"]["explanation"] = "The domain of the input URL is in the whitelist (safe)"
        response["predict"]["result"] = -1
        response["predict"]["explanation"] = "The domain of the input URL is already in the whitelist (safe), no prediction needed"

    elif isBlacklist == 1:
        response["blacklist"]["explanation"] = "The domain of the input URL is in the blacklist (malicious)"
        response["predict"]["result"] = -1
        response["predict"]["explanation"] = "The domain of the input URL is already in the blacklist (malicious), no prediction needed"
    
    else:
        response["blacklist"]["explanation"] = "The domain of the input URL is neither in the blacklist nor the whitelist"
        
        # predict the input URL
        data = {'url':[url],
                'shorten':[shortening_service(url)],
                'age':[whoisAge(url)],
                'response':[responseTime(url)],
                'alexa':[alexaRank(url)]}

        dataFrame = pd.DataFrame(data)
        transformedUrl = vectorizer.transform(dataFrame)
        [result] = classifier.predict(transformedUrl)

        response["predict"]["result"] = int(result)
        if result:
            response["predict"]["explanation"] = "The classifier predicts the input URL is a malicious URL"
        else:
            response["predict"]["explanation"] = "The classifier predicts the input URL is a safe URL"

    return flask.jsonify(response)

app.run(host='0.0.0.0')
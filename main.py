import flask
import joblib

from services import getURLength, getDomainLength, getDotNum, getPathLength, getPercentNum, getAtNum, getSlashNum, getURLength, getWordsFromURL, changeContent

# app configuration
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['JSON_SORT_KEYS'] = False

# load models
decesionTreeModel = joblib.load('./src/models/decesionTree.pkl')
logisticRegressionModel = joblib.load('./src/models/logisticRegression.pkl')
randomForestModel = joblib.load('./src/models/randomForest.pkl')
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
        "url": url,
        "predict": [
            {
                "model": None,
                "result": None,
                "explanation": None
            },
            {
                "model": None,
                "result": None,
                "explanation": None
            },
            {
                "model": None,
                "result": None,
                "explanation": None
            }
        ]
    }

    transformedUrl = vectorizer.transform([url])
    resultBydecesionTree = decesionTreeModel.predict(transformedUrl)
    resultByLogisticRegression = logisticRegressionModel.predict(transformedUrl)
    resultByRandomForest = randomForestModel.predict(transformedUrl)

    results = [resultBydecesionTree[0], resultByLogisticRegression[0], resultByRandomForest[0]]
    results = map(int, results)
    
    for index, result in enumerate(results):
        response["predict"][index]["model"] = listOfModels[index]
        response["predict"][index]["result"] = result
        if result:
            response["predict"][index]["explanation"] = f"The {listOfModels[index]} model predicts the input URL is a malicious URL"
        else:
            response["predict"][index]["explanation"] = f"The {listOfModels[index]} model predicts the input URL is a benign URL"

    return flask.jsonify(response)

app.run(host='0.0.0.0')
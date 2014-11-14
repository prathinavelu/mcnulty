import flask
import numpy as np
from sklearn.linear_model import LogisticRegression

app = flask.Flask("OMGApp")

X = np.linspace(1,1000,50).reshape(-1,1)
Y = np.zeros(50,)
Y[25:] = np.ones(25,)
PREDICTOR = LogisticRegression().fit(X,Y)

@app.route("/predict", methods=["POST"])
def predict():

    data = flask.request.json

    x = np.array( data["example"] ).reshape(-1,1)    
    y_pred = PREDICTOR.predict(x)
    y_pred = list(y_pred)

    results = {"predicted": y_pred}
    
    return flask.jsonify(results)

@app.route("/")
def hello():
    return "It's alive!"

@app.route("/gabe")
def gabe():
    page = "<html>"
    page += "<body>"
    page += "<p> Hiiii! I am <strong>GABE</strong>. Helloo.</p>"
    page += "</body>"
    page += "</html>"
    return page

app.debug = True

app.run()

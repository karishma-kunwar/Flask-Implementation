
from distutils.log import debug
import numpy as np
from flask import Flask,render_template,request
from sklearn.preprocessing import StandardScaler
import joblib


model = joblib.load('LogisticRegression_model.pkl')
app = Flask(__name__)

standard_to = StandardScaler()

@app.route('/')

def home():
    return render_template("index.html")


@app.route('/predict',methods= ['POST'])

def predict():

    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    final_features_scaled = standard_to.fit_transform(final_features)
    prediction = model.predict(final_features_scaled)

    if (prediction == True):
        result = "It is a Prepaid condition"
    
    elif (prediction == False):
        result = "It is Non-prepaid condition"

    else:
        result = "Not available"

    return render_template("index.html", result= result)



if __name__ == "__main__":

    app.run()
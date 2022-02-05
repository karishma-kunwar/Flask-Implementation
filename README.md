## <b>Mortage prepayment prediction Application</b>

This application is a simple mortage prepayment application which uses a ML trained model to predict weather a person prepays the mortage earlier their allocated time. By using such prediction model banks prevent the risk that can occure.

### <u> Description of the web application </u>
The web application uses simple techniques for it's implementaion.

* <b> HTML & CSS</b> for the fromend part.
* <b> Flask </b> is used in backend.


### Workflow of the project

The user inputs necessary data into the form like structure and once click the predict button the result is displayed on the screen itself. 

Logic behind:

The main file that we need o focus on is app.py. 

STEP 1:  
We have done necessary imports of the library that we need to implement our logic.

```python
from distutils.log import debug
import numpy as np
from flask import Flask,render_template,request
from sklearn.preprocessing import StandardScaler
import joblib

```


STEP 2:  
After that we read the pickled file using the Joblib library.

STEP 3:

Then we define a function named predict prepayment where we basically take in the input from the user and then convert the input into the float format and then scale down the value and finally call the <b>.predict</b>  function which does the prediction job.


```python
# Demo

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


```

### Screenshot of the project

#### UI of the project

![image](https://user-images.githubusercontent.com/57294017/152632487-700ded30-d8a4-4fbb-970a-621e81188562.png)


![image](https://user-images.githubusercontent.com/57294017/152632519-f5a1abcb-148a-4d1b-b7d9-dce301012c51.png)

![image](https://user-images.githubusercontent.com/57294017/152632529-c4696a71-0b27-4188-97f0-6fb675cce0d5.png)


### Result for the prediction

![image](https://user-images.githubusercontent.com/57294017/152632650-bc9f5520-23d1-4b6a-8912-0e2d7c930562.png)

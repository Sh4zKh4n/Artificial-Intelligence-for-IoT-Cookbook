from flask import Flask, request, jsonify
import os
import pickle
import pandas as pd
import xgboost as xgb


application = Flask(__name__)
model_filename = os.path.join(os.getcwd(), 'bst.sav')
loaded_model = pickle.load(open(model_filename, "rb"))

@application.route('/predict', methods=['POST']) 
def predict():
    
    x_test = pd.DataFrame(request.json)
    y_pred = loaded_model.predict(xgb.DMatrix(x_test))
    y_pred[y_pred > 0.5] = 1
    y_pred[y_pred <= 0.5] = 0
    return int(y_pred[0])

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8000)


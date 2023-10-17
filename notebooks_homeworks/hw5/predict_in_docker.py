import pickle
from flask import Flask
from flask import request
from flask import jsonify

with open('dv.bin','rb') as f_in_dv:
    dv = pickle.load(f_in_dv)

with open('model2.bin','rb') as f_in_model1:
    model = pickle.load(f_in_model1)


app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    will_get_credit = y_pred >= 0.5
    
    result = {
        'probability': y_pred,
        'will_get_credit': bool(will_get_credit)
    }

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)  
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Take list of args in params
@app.route('/predict', methods=['GET'])
def predict():
    try:
        params = {
            "age": request.args.get('age'),
            "sex": request.args.get('sex'),
            "bmi": request.args.get('bmi'),
            "children": request.args.get('children'),
            "smoker": request.args.get('smoker'),
            "region": request.args.get('region')
        }

        # prediction = subprocess(....) (pipe)
        
        return params, 200
    except Exception as e:
        raise f"[ERROR] predict request: {e}"

# Take json object in params  
@app.route('/retrain', methods=['POST'])
def retrain():
    try:
        data = request.json
        df = pd.DataFrame(data)

        #jsons = df.to_json(index=False) ... to convert data in json

        #new_score = .... (pipe)
        
        return jsons, 200
    except Exception as e:
        raise f"[ERROR] retrain request: {e}"
    
if __name__ == '__main__':
    app.run(debug=True)

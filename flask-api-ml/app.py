from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        features = pd.DataFrame([data])
        # Placeholder for prediction logic
        prediction = make_prediction(model, features)
        return jsonify({'prediction': str(prediction)})

# Take json object in params


@app.route('/retrain', methods=['POST'])
def retrain():
    try:
        data = request.json
        df = pd.DataFrame(data)

        # jsons = df.to_json(index=False) ... to convert data in json

        # new_score = .... (pipe)

        return jsons, 200
    except Exception as e:
        raise f"[ERROR] retrain request: {e}"


if __name__ == '__main__':
    app.run(debug=True)

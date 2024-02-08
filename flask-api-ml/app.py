from flask import Flask, request, render_template, redirect, url_for
from model.src.model_dev import ModelDevelopment

app = Flask(__name__)

class PredictionParams:
    def __init__(self, age, sex, bmi, children, smoker, region):
        self.age = age,
        self.sex = sex,
        self.bmi = bmi,
        self.children = children,
        self.smoker = smoker,
        self.region = region
    
    def prediction(self):
        model = ModelDevelopment().load_model("model/saved_model/trained_model.pkl")

        return f"{self.age} / {self.sex} / {self.bmi} / {self.children} / {self.smoker} / {self.region} == "

# In-memory database
predictions = []

@app.route('/')
def index():
    return render_template('index.html', items=predictions)

@app.route('/predict', methods=['POST'])
def predict():
    age = request.form.get('age')
    sex = request.form.get('sex')
    bmi = request.form.get('bmi')
    children = request.form.get('children')
    smoker = request.form.get('smoker')
    region = request.form.get('region')
    if age & sex & bmi & children & smoker & region:
        params = PredictionParams(age, sex, bmi, children, smoker, region)
        predictions.append(item)
    return redirect(url_for('index'))


@app.route('/get')
def get():
    return predictions
"""
@app.route('/add', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete_item(index):
    if index < len(items):
        items.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update_item(index):
    if index < len(items):
        items[index] = request.form.get('new_item')
    return redirect(url_for('index'))
"""
if __name__ == '__main__':
    app.run(debug=True)

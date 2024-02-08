from pathlib import Path

from zenml import pipeline

from steps.data_loader import load_data
from steps.preprocessor import preprocess_data
from steps.model_trainer import train_model
from steps.evaluator import evaluate_model


@pipeline
def training_pipeline():

    input_data_path = Path('./data/insurance.csv')
    data = load_data(str(input_data_path))

    X_train, X_test, y_train, y_test = preprocess_data(data)

    model_output_path = train_model(X_train=X_train, y_train=y_train)

    evaluate_model(model_output_path=model_output_path, X_test=X_test, y_test=y_test)

from zenml.pipelines import pipeline

import pandas as pd

from steps.preprocessor import preprocess_data
from steps.model_trainer import train_model
from steps.evaluator import evaluate_model


@pipeline
def insurance_charges_prediction_pipeline(
    preprocess_step,
    train_step,
    evaluate_step,
):
    """Defines the pipeline for predicting insurance charges."""
    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_step()

    # Train the model
    model_path = train_step(X_train=X_train, y_train=y_train)

    # Evaluate the model
    evaluate_step(model_path=model_path, X_test=X_test, y_test=y_test)


# Assuming you have loaded your dataset into a DataFrame `df`
# and your steps are properly implemented and imported
if __name__ == "__main__":
    # Load dataset
    df = pd.read_csv('path/to/your/dataset.csv')

    # Define the pipeline
    pipeline_instance = insurance_charges_prediction_pipeline(
        preprocess_step=preprocess_data(df=df),
        train_step=train_model(),
        evaluate_step=evaluate_model(),
    )

    # Run the pipeline
    pipeline_instance.run()

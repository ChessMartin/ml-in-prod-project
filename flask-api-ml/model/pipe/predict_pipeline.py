from zenml import pipeline 
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.prediction import prediction_model
from steps.evaluation import evaluate_model

@pipeline(enable_cache=True)
def predict_pipeline(data_path: str):
    """
    Training pipeline for the model
    """
    # Ingest data
    df = ingest_df(data_path)  # 1)
    
    # Clean and split data
    X_train, X_test, y_train, y_test = clean_df(df)  # 2)
    
    # Train model with training data
    prediction = prediction_model()
    
    return prediction


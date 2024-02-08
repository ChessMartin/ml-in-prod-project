import logging
from zenml import step
from src.evaluation import ModelEvaluation
import pandas as pd

@step
def prediction_model(
    model, 
    X_test: pd.DataFrame, 
) -> float:
    """
    Evaluate the trained model with test data.

    Args:
        model_path: Path to the saved trained model.
        X_test: Testing data features.
        y_test: Testing data target.

    Returns:
        r2: R-squared, coefficient of determination.
    """
    try:
        # Predict value
        predict = ModelEvaluation.predict_model(model, X_test)  # Directly receive R^2
        
        # Log only the R-squared metric
        logging.info(f"Model prediction: {predict}")
        
        # Return only the R-squared metric
        return predict
    except Exception as e:
        logging.error(f"Error in model evaluation: {e}")
        raise e
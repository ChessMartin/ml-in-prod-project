import pandas as pd
import numpy as np

from ..steps.evaluator import evaluate_model


def test_evaluate_model(trained_model_path):
    X_test = pd.DataFrame(np.random.rand(5, 5))
    y_test = pd.Series(np.random.rand(5))

    metrics = evaluate_model(model_output_path=trained_model_path, X_test=X_test, y_test=y_test)

    assert 'MSE' in metrics, "Accuracy should be calculated"
    assert metrics['MSE'] > 0, "Accuracy should be greater than 0"

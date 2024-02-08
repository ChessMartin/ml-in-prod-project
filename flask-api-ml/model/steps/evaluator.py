from pathlib import Path
import joblib
import json

from zenml import step

import pandas as pd

from sklearn.metrics import mean_absolute_error, mean_squared_error


@step
def evaluate_model(model_output_path: Path, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    model = joblib.load(model_output_path)
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    metrics = {'MSE': mse, 'MAE': mae}

    eval_dir = Path('evaluations')
    eval_dir.mkdir(exist_ok=True)

    metrics_output_filename = model_output_path.with_suffix('.json').name
    metrics_path = eval_dir / metrics_output_filename

    with metrics_path.open('w') as f:
        json.dump(metrics, f)

    print(f'Metrics saved to {metrics_path}')
    return metrics

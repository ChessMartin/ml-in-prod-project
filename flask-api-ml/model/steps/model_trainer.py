from datetime import datetime
from pathlib import Path
import joblib

from zenml import step

import pandas as pd

from sklearn.ensemble import RandomForestRegressor


@step
def train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Path:
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    models_dir = Path('models')
    models_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    model_output_path = Path(models_dir / f'random_forest_{timestamp}.joblib')
    joblib.dump(model, model_output_path)

    return model_output_path

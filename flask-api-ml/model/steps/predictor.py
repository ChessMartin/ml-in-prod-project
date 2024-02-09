from pathlib import Path
from typing import Optional
import joblib
import json

from zenml import step
import pandas as pd

MODELS_DIR = Path("./models/")


def get_latest_model_path(models_dir: str) -> Optional[Path]:
    models_path = Path(models_dir)
    models = list(models_path.glob('*.joblib'))
    if not models:
        return None
    latest_model = max(models, key=lambda x: x.stat().st_mtime)
    return latest_model


@step
def predict(input_json_filepath: Path, ) -> int:
    with open(input_json_filepath, 'r') as f:
        input_data = json.load(f)
    input_df = pd.DataFrame([input_data])

    model_path = get_latest_model_path(MODELS_DIR)
    if model_path is None:
        raise FileNotFoundError("No model found in the specified directory.")

    model = joblib.load(model_path)
    predictions = model.predict(input_df)

    print(predictions)

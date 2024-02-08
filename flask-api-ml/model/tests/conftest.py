import pytest

from pathlib import Path
import pandas as pd
import numpy as np

from ..steps.model_trainer import train_model


@pytest.fixture(scope="session")
def trained_model_path() -> Path:
    X_train = pd.DataFrame(np.random.rand(100, 5))
    y_train = pd.Series(np.random.rand(100))

    model_path = train_model(X_train=X_train, y_train=y_train)

    return model_path

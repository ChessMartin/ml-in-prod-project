import pandas as pd
import numpy as np

from ..steps.model_trainer import train_model


def test_train_model():
    X_train = pd.DataFrame(np.random.rand(10, 5))
    y_train = pd.Series(np.random.rand(10))

    model_path = train_model(X_train=X_train, y_train=y_train)

    assert model_path.exists(), "Model should be saved to disk"

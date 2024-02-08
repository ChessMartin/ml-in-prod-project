from ..steps.preprocessor import preprocess_data
import pandas as pd


def test_preprocess_data():
    # Example test data
    test_data = pd.DataFrame({
        'age': [19, 50],
        'sex': ['female', 'male'],
        'bmi': [27.9, 30.5],
        'children': [0, 2],
        'smoker': ['yes', 'no'],
        'region': ['southwest', 'southeast'],
        'charges': [16884.924, 12629.165],
    })

    X_train, X_test, y_train, y_test = preprocess_data(df=test_data)

    assert not X_train.empty and not X_test.empty, "DataFrames should not be empty"
    assert not y_train.empty and not y_test.empty, "Series should not be empty"

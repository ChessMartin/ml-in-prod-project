from zenml import step

from typing import Tuple, Annotated
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


@step
def preprocess_data(
    df: pd.DataFrame
) -> Tuple[
    Annotated[pd.DataFrame, 'X_train'],
    Annotated[pd.DataFrame, 'X_test'],
    Annotated[pd.Series, 'y_train'],
    Annotated[pd.Series, 'y_test']
]:
    X = df.drop('charges', axis=1)
    y = df['charges']

    numerical_cols = ['age', 'bmi', 'children']
    categorical_cols = ['sex', 'smoker', 'region']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(), categorical_cols)
        ])

    X_processed = preprocessor.fit_transform(X)
    columns = (
        numerical_cols + list(
            preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_cols)
        )
    )
    X_processed = pd.DataFrame(X_processed, columns=columns)

    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test

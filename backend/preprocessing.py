import joblib
import pandas as pd

from backend.config import PREPROCESSOR_PATH


# Load preprocessor
preprocessor = joblib.load(
    PREPROCESSOR_PATH
)


def preprocess_input(data):

    # Convert dictionary into DataFrame
    df = pd.DataFrame([data])

    # Apply saved preprocessing
    processed_data = preprocessor.transform(df)

    return processed_data
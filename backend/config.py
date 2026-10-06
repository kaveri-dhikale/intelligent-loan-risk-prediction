from pathlib import Path


# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Model directory
MODEL_DIR = BASE_DIR / "models"


# Model files
MODEL_PATH = MODEL_DIR / "loan_model.pkl"

PREPROCESSOR_PATH = MODEL_DIR / "preprocessor.pkl"

FEATURE_COLUMNS_PATH = MODEL_DIR / "feature_columns.pkl"

METADATA_PATH = MODEL_DIR / "model_metadata.pkl"
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

import pandas as pd
import numpy as np
import joblib
import os


# ============================================================
# 1. CREATE FASTAPI APPLICATION
# ============================================================

app = FastAPI(
    title="Intelligent Loan Approval & Credit Risk Prediction API",
    description="Loan approval prediction using Random Forest",
    version="1.0.0"
)


# ============================================================
# 2. DEFINE MODEL PATHS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)


# ============================================================
# 3. LOAD MODEL ARTIFACTS
# ============================================================

model = joblib.load(
    os.path.join(MODEL_DIR, "loan_model.pkl")
)

preprocessor = joblib.load(
    os.path.join(MODEL_DIR, "preprocessor.pkl")
)

feature_selector = joblib.load(
    os.path.join(MODEL_DIR, "feature_selector.pkl")
)

raw_feature_columns = joblib.load(
    os.path.join(MODEL_DIR, "raw_feature_columns.pkl")
)

print("All model files loaded successfully!")


# ============================================================
# 4. REQUEST FORMAT
# ============================================================

class LoanRequest(BaseModel):

    features: Dict[str, Any]


# ============================================================
# 5. HEALTH CHECK API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "Loan Approval Prediction API is running",
        "status": "success"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "model": "Random Forest"
    }


# ============================================================
# 6. PREDICTION API
# ============================================================

@app.post("/predict")
def predict_loan(request: LoanRequest):

    try:

        input_data = request.features

        # Check missing columns
        missing_columns = [
            col for col in raw_feature_columns
            if col not in input_data
        ]

        if missing_columns:

            raise HTTPException(
                status_code=400,
                detail={
                    "message": "Missing input columns",
                    "missing_columns": missing_columns
                }
            )

        # Create DataFrame in training column order
        input_df = pd.DataFrame(
            [input_data],
            columns=raw_feature_columns
        )

        # Preprocess input
        processed_data = preprocessor.transform(
            input_df
        )

        # Select features
        selected_data = feature_selector.transform(
            processed_data
        )

        # Make prediction
        prediction = model.predict(
            selected_data
        )[0]

        # Calculate probability
        probabilities = model.predict_proba(
            selected_data
        )[0]

        approval_probability = float(
            probabilities[1]
        )

        rejection_probability = float(
            probabilities[0]
        )

        # Determine approval status
        if int(prediction) == 1:

            approval_status = "Approved"

        else:

            approval_status = "Rejected"

        # Determine risk level
        if approval_probability >= 0.70:

            risk_level = "Low"

        elif approval_probability >= 0.40:

            risk_level = "Medium"

        else:

            risk_level = "High"

        return {

            "prediction": int(prediction),

            "approval_status": approval_status,

            "approval_probability": round(
                approval_probability * 100,
                2
            ),

            "rejection_probability": round(
                rejection_probability * 100,
                2
            ),

            "risk_level": risk_level

        }

    except HTTPException:

        raise

    except Exception as error:

        raise HTTPException(

            status_code=500,

            detail=str(error)

        )


# ============================================================
# 7. RUN SERVER
# ============================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000
    )
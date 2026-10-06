import joblib

from backend.config import MODEL_PATH
from backend.preprocessing import preprocess_input


# Load trained model
model = joblib.load(
    MODEL_PATH
)


def predict_loan(data):

    # Preprocess input
    processed_data = preprocess_input(data)

    # Make prediction
    prediction = model.predict(
        processed_data
    )[0]

    # Get probability
    probabilities = model.predict_proba(
        processed_data
    )[0]

    # Get probability of class 1
    approval_probability = probabilities[1] * 100

    # Example risk mapping
    if approval_probability >= 70:
        risk_level = "Low"

    elif approval_probability >= 40:
        risk_level = "Medium"

    else:
        risk_level = "High"

    return {
        "prediction": int(prediction),
        "approval_probability": round(
            approval_probability,
            2
        ),
        "risk_level": risk_level
    }
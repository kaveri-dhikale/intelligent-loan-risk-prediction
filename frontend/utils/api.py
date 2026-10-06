import requests


API_URL = "http://127.0.0.1:8000"


def check_api_health():
    """
    Check whether the FastAPI backend is available.
    """

    try:
        response = requests.get(
            f"{API_URL}/health",
            timeout=5
        )

        if response.status_code == 200:
            return True, response.json()

        return False, None

    except requests.exceptions.RequestException:
        return False, None


def predict_loan(features):
    """
    Send applicant features to FastAPI
    and return the prediction response.
    """

    try:

        response = requests.post(
            f"{API_URL}/predict",
            json={
                "features": features
            },
            timeout=30
        )

        if response.status_code == 200:

            return {
                "success": True,
                "data": response.json(),
                "error": None
            }

        try:
            error_detail = response.json()

        except Exception:
            error_detail = response.text

        return {
            "success": False,
            "data": None,
            "error": error_detail
        }

    except requests.exceptions.ConnectionError:

        return {
            "success": False,
            "data": None,
            "error": (
                "Unable to connect to the FastAPI backend. "
                "Please make sure the backend is running on port 8000."
            )
        }

    except requests.exceptions.Timeout:

        return {
            "success": False,
            "data": None,
            "error": "The prediction service took too long to respond."

        }

    except requests.exceptions.RequestException as error:

        return {
            "success": False,
            "data": None,
            "error": str(error)
        }
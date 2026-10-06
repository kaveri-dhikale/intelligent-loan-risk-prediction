
import streamlit as st
from utils.api import predict_loan


def show_prediction():
    st.title("📝 Loan Prediction")
    st.markdown(
        "Enter the applicant's financial and credit information to "
        "estimate loan approval risk."
    )

    st.divider()

    # =========================================================
    # PERSONAL INFORMATION
    # =========================================================
    st.subheader("👤 Personal Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input(
            "Age",
            min_value=18,
            max_value=80,
            value=30,
            step=1
        )

    with col2:
        employment_status = st.selectbox(
            "Employment Status",
            ["Employed", "Self-Employed", "Unemployed"]
        )

    with col3:
        experience = st.number_input(
            "Experience (Years)",
            min_value=0.0,
            max_value=50.0,
            value=5.0,
            step=0.5
        )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        education_level = st.selectbox(
            "Education Level",
            [
                "High School",
                "Associate",
                "Bachelor",
                "Master",
                "Doctorate"
            ]
        )

    with col2:
        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married", "Divorced", "Widowed"]
        )

    with col3:
        dependents = st.number_input(
            "Number of Dependents",
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

    with col4:
        home_ownership = st.selectbox(
            "Home Ownership",
            ["Rent", "Own", "Mortgage", "Other"]
        )

    st.divider()

    # =========================================================
    # INCOME & FINANCIAL PROFILE
    # =========================================================
    st.subheader("💰 Income & Financial Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        annual_income = st.number_input(
            "Annual Income (₹)",
            min_value=0.0,
            max_value=100000000.0,
            value=600000.0,
            step=10000.0
        )

    with col2:
        savings = st.number_input(
            "Savings Account Balance (₹)",
            min_value=0.0,
            max_value=100000000.0,
            value=100000.0,
            step=5000.0
        )

    with col3:
        checking = st.number_input(
            "Checking Account Balance (₹)",
            min_value=0.0,
            max_value=100000000.0,
            value=50000.0,
            step=5000.0
        )

    col1, col2 = st.columns(2)

    with col1:
        total_assets = st.number_input(
            "Total Assets (₹)",
            min_value=0.0,
            max_value=500000000.0,
            value=500000.0,
            step=10000.0
        )

    with col2:
        total_liabilities = st.number_input(
            "Total Liabilities (₹)",
            min_value=0.0,
            max_value=500000000.0,
            value=100000.0,
            step=10000.0
        )

    # Automatically calculated
    monthly_income = annual_income / 12
    net_worth = total_assets - total_liabilities

    st.info(
        f"Monthly Income: ₹{monthly_income:,.2f}  |  "
        f"Estimated Net Worth: ₹{net_worth:,.2f}"
    )

    st.divider()

    # =========================================================
    # CREDIT PROFILE
    # =========================================================
    st.subheader("💳 Credit Profile")

    col1, col2, col3 = st.columns(3)

    with col1:
        credit_score = st.number_input(
            "Credit Score",
            min_value=300,
            max_value=900,
            value=700,
            step=1
        )

    with col2:
        credit_utilization = st.number_input(
            "Credit Card Utilization",
            min_value=0.0,
            max_value=1.0,
            value=0.30,
            step=0.01
        )

    with col3:
        payment_history = st.number_input(
            "Payment History",
            min_value=0.0,
            max_value=1.0,
            value=0.90,
            step=0.01
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        previous_defaults = st.selectbox(
            "Previous Loan Defaults",
            ["No", "Yes"]
        )

    with col2:
        bankruptcy_history = st.selectbox(
            "Bankruptcy History",
            ["No", "Yes"]
        )

    with col3:
        credit_history_length = st.number_input(
            "Length of Credit History (Years)",
            min_value=0.0,
            max_value=60.0,
            value=8.0,
            step=0.5
        )

    st.divider()

    # =========================================================
    # LOAN DETAILS
    # =========================================================
    st.subheader("🏦 Loan Details")

    col1, col2, col3 = st.columns(3)

    with col1:
        loan_amount = st.number_input(
            "Loan Amount (₹)",
            min_value=0.0,
            max_value=100000000.0,
            value=300000.0,
            step=10000.0
        )

    with col2:
        loan_duration = st.number_input(
            "Loan Duration (Months)",
            min_value=1,
            max_value=360,
            value=36,
            step=1
        )

    with col3:
        loan_purpose = st.selectbox(
            "Loan Purpose",
            [
                "Auto",
                "Debt Consolidation",
                "Education",
                "Home",
                "Other"
            ]
        )

    col1, col2 = st.columns(2)

    with col1:
        monthly_debt = st.number_input(
            "Monthly Debt Payments (₹)",
            min_value=0.0,
            max_value=10000000.0,
            value=10000.0,
            step=1000.0
        )

    with col2:
        dti = st.number_input(
            "Debt-to-Income Ratio",
            min_value=0.0,
            max_value=1.0,
            value=0.30,
            step=0.01
        )

    st.caption(
        "💡 For ratio fields, enter values between 0 and 1. "
        "For example, 30% should be entered as 0.30."
    )

    st.divider()

    # =========================================================
    # PREDICTION
    # =========================================================
    if st.button(
        "🔮 Predict Loan Risk",
        use_container_width=True,
        type="primary"
    ):

        # Convert Yes/No values to the numerical representation
        # used by the trained model.
        previous_defaults_value = (
            1 if previous_defaults == "Yes" else 0
        )

        bankruptcy_value = (
            1 if bankruptcy_history == "Yes" else 0
        )

        # Job tenure is derived from experience.
        # This avoids asking the user for another similar field.
        job_tenure = min(experience, max(0.0, experience * 0.75))

        # Open credit lines and inquiries are not displayed
        # because they are secondary inputs for this simplified UI.
        open_credit_lines = 5
        credit_inquiries = 2

        # Utility payment history follows the applicant's
        # general payment history.
        utility_payment_history = payment_history

        # Build all 29 features expected by the trained model.
        features = {
            "Age": age,
            "AnnualIncome": annual_income,
            "CreditScore": credit_score,
            "EmploymentStatus": employment_status,
            "EducationLevel": education_level,
            "Experience": experience,
            "LoanAmount": loan_amount,
            "LoanDuration": loan_duration,
            "MaritalStatus": marital_status,
            "NumberOfDependents": dependents,
            "HomeOwnershipStatus": home_ownership,
            "MonthlyDebtPayments": monthly_debt,
            "CreditCardUtilizationRate": credit_utilization,
            "NumberOfOpenCreditLines": open_credit_lines,
            "NumberOfCreditInquiries": credit_inquiries,
            "DebtToIncomeRatio": dti,
            "BankruptcyHistory": bankruptcy_value,
            "LoanPurpose": loan_purpose,
            "PreviousLoanDefaults": previous_defaults_value,
            "PaymentHistory": payment_history,
            "LengthOfCreditHistory": credit_history_length,
            "SavingsAccountBalance": savings,
            "CheckingAccountBalance": checking,
            "TotalAssets": total_assets,
            "TotalLiabilities": total_liabilities,
            "MonthlyIncome": monthly_income,
            "UtilityBillsPaymentHistory": utility_payment_history,
            "JobTenure": job_tenure,
            "NetWorth": net_worth
        }

        try:
            result = predict_loan(features)

            # Store result in session state
            st.session_state["prediction_result"] = result
            st.session_state["applicant_features"] = features

        except Exception as e:
            st.error(f"Prediction failed: {str(e)}")

    # =========================================================
    # DISPLAY RESULT
    # =========================================================
    if "prediction_result" in st.session_state:

        
        result = st.session_state["prediction_result"]

        # The API response is wrapped inside "data"
        if result.get("success"):

            data = result.get("data", {})

            decision = data.get(
                "approval_status",
                "Unknown"
            )

            approval_probability = float(
                data.get("approval_probability", 0)
            )

            rejection_probability = float(
                data.get("rejection_probability", 0)
            )

            risk_level = data.get(
                "risk_level",
                "Unknown"
            )

        else:
            st.error(
            f"Prediction failed: {result.get('error', 'Unknown error')}"
            )
            return


        # Result cards
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Decision",
                decision
            )

        with col2:
            st.metric(
                "Approval Probability",
                f"{approval_probability:.2f}%"
            )

        with col3:
            st.metric(
                "Risk Level",
                risk_level
            )

        st.subheader("📊 Prediction Probability")

        st.progress(
            min(max(approval_probability / 100, 0.0), 1.0)
        )

        col1, col2 = st.columns(2)

        with col1:
            st.write(
                f"**Approval:** {approval_probability:.2f}%"
            )

        with col2:
            st.write(
                f"**Rejection:** {rejection_probability:.2f}%"
            )

        st.subheader("💡 Assessment")

        if approval_probability >= 70:
            st.success(
                "The model predicts a high probability of loan approval "
                "with a relatively low level of financial risk."
            )

        elif approval_probability >= 40:
            st.warning(
                "The model predicts a moderate probability of loan approval "
                "and indicates a medium level of financial risk."
            )

        else:
            st.error(
                "The model predicts a low probability of loan approval "
                "and a relatively high level of financial risk."
            )

        st.caption(
            "⚠️ This prediction is generated by a machine learning model "
            "and should not be treated as a final lending decision."
        )


# ### Then restart Streamlit

# In your PowerShell:

# ```powershell
# Ctrl + C
# ```

# Then:

# ```powershell
# streamlit run frontend/app.py
# ```

# ### Important change

# Your backend still receives **all 29 features**, so you don't need to modify:

# * `backend/main.py`
# * `loan_model.pkl`
# * `preprocessor.pkl`
# * `feature_selector.pkl`
# * `raw_feature_columns.pkl`

# Only `prediction.py` changes.

# ### Test it first with this applicant

# Use these values:

# | Field              |      Value |
# | ------------------ | ---------: |
# | Age                |         35 |
# | Employment         |   Employed |
# | Experience         |         10 |
# | Education          |   Bachelor |
# | Marital            |    Married |
# | Dependents         |          0 |
# | Home               |        Own |
# | Annual Income      | ₹1,200,000 |
# | Savings            |   ₹240,000 |
# | Checking           |   ₹150,000 |
# | Assets             |   ₹500,000 |
# | Liabilities        |    ₹60,000 |
# | Credit Score       |        800 |
# | Credit Utilization |       0.20 |
# | Payment History    |       0.95 |
# | Previous Defaults  |         No |
# | Bankruptcy         |         No |
# | Credit History     |         17 |
# | Loan Amount        |   ₹200,000 |
# | Duration           |         36 |
# | Purpose            |       Home |
# | Monthly Debt       |     ₹5,000 |
# | DTI                |       0.15 |

# **One note:** `JobTenure`, `NumberOfOpenCreditLines`, `NumberOfCreditInquiries`, and `UtilityBillsPaymentHistory` are still derived/defaulted because we are trying to keep the form manageable. If the results remain unexpectedly low, we can make those four inputs visible next rather than guessing them.

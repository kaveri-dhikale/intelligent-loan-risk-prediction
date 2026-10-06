import streamlit as st
import plotly.graph_objects as go


def show_risk_analysis():

    # =====================================================
    # CHECK PREDICTION DATA
    # =====================================================

    if "prediction_result" not in st.session_state:

        st.title("📊 Risk Analysis")

        st.warning(
            "No prediction data available. "
            "Please complete a loan prediction first."
        )

        st.info(
            "Go to the Loan Prediction page, enter applicant "
            "details, and click Analyze Loan Risk."
        )

        return

    # =====================================================
    # GET STORED DATA
    # =====================================================

    prediction_data = st.session_state["prediction_result"]

    applicant_features = st.session_state.get(
        "applicant_features",
        {}
    )

    approval_status = prediction_data.get(
        "approval_status",
        "Unknown"
    )

    approval_probability = float(
        prediction_data.get(
            "approval_probability",
            0
        )
    )

    rejection_probability = float(
        prediction_data.get(
            "rejection_probability",
            0
        )
    )

    risk_level = prediction_data.get(
        "risk_level",
        "Unknown"
    )

    # =====================================================
    # PAGE HEADER
    # =====================================================

    st.title("📊 Risk Analysis")

    st.write(
        "Analyze the applicant's financial profile, "
        "credit information, and predicted loan risk."
    )

    st.divider()

    # =====================================================
    # RISK SUMMARY
    # =====================================================

    st.subheader("📋 Risk Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        if approval_status == "Approved":

            st.success(
                f"Decision: {approval_status}"
            )

        else:

            st.error(
                f"Decision: {approval_status}"
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

    st.divider()

    # =====================================================
    # APPROVAL VS REJECTION DOUGHNUT CHART
    # =====================================================

    st.subheader("🍩 Approval vs. Rejection Probability")

    chart_data = [
        approval_probability,
        rejection_probability
    ]

    chart_labels = [
        "Approval",
        "Rejection"
    ]

    figure = go.Figure(
        data=[
            go.Pie(
                labels=chart_labels,
                values=chart_data,
                hole=0.55,
                textinfo="label+percent",
                hovertemplate=(
                    "%{label}: %{value:.2f}%"
                    "<extra></extra>"
                )
            )
        ]
    )

    figure.update_layout(
        title="Loan Prediction Probability",
        height=400,
        showlegend=True,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )

    st.divider()

    # =====================================================
    # FINANCIAL OVERVIEW
    # =====================================================

    st.subheader("💰 Financial Overview")

    annual_income = applicant_features.get(
        "AnnualIncome",
        0
    )

    monthly_income = applicant_features.get(
        "MonthlyIncome",
        0
    )

    loan_amount = applicant_features.get(
        "LoanAmount",
        0
    )

    total_assets = applicant_features.get(
        "TotalAssets",
        0
    )

    total_liabilities = applicant_features.get(
        "TotalLiabilities",
        0
    )

    net_worth = applicant_features.get(
        "NetWorth",
        0
    )

    monthly_debt = applicant_features.get(
        "MonthlyDebtPayments",
        0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Annual Income",
            f"₹{annual_income:,.2f}"
        )

    with col2:

        st.metric(
            "Monthly Income",
            f"₹{monthly_income:,.2f}"
        )

    with col3:

        st.metric(
            "Loan Amount",
            f"₹{loan_amount:,.2f}"
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Assets",
            f"₹{total_assets:,.2f}"
        )

    with col2:

        st.metric(
            "Total Liabilities",
            f"₹{total_liabilities:,.2f}"
        )

    with col3:

        st.metric(
            "Net Worth",
            f"₹{net_worth:,.2f}"
        )

    st.caption(
        "Currency symbols and units should match the "
        "currency and units used in your training dataset."
    )

    st.divider()

    # =====================================================
    # CREDIT PROFILE
    # =====================================================

    st.subheader("💳 Credit Profile")

    credit_score = applicant_features.get(
        "CreditScore",
        0
    )

    credit_utilization = applicant_features.get(
        "CreditCardUtilizationRate",
        0
    )

    payment_history = applicant_features.get(
        "PaymentHistory",
        0
    )

    credit_history_length = applicant_features.get(
        "LengthOfCreditHistory",
        0
    )

    open_credit_lines = applicant_features.get(
        "NumberOfOpenCreditLines",
        0
    )

    credit_inquiries = applicant_features.get(
        "NumberOfCreditInquiries",
        0
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Credit Score",
            f"{credit_score}"
        )

    with col2:

        st.metric(
            "Credit Utilization",
            f"{credit_utilization:.2f}"
        )

    with col3:

        st.metric(
            "Payment History",
            f"{payment_history:.2f}"
        )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Credit History",
            f"{credit_history_length} years"
        )

    with col2:

        st.metric(
            "Open Credit Lines",
            f"{open_credit_lines}"
        )

    with col3:

        st.metric(
            "Credit Inquiries",
            f"{credit_inquiries}"
        )

    st.divider()

    # =====================================================
    # APPLICANT SUMMARY
    # =====================================================

    st.subheader("👤 Applicant Summary")

    age = applicant_features.get(
        "Age",
        "Not available"
    )

    education = applicant_features.get(
        "EducationLevel",
        "Not available"
    )

    employment_status = applicant_features.get(
        "EmploymentStatus",
        "Not available"
    )

    experience = applicant_features.get(
        "Experience",
        "Not available"
    )

    job_tenure = applicant_features.get(
        "JobTenure",
        "Not available"
    )

    marital_status = applicant_features.get(
        "MaritalStatus",
        "Not available"
    )

    dependents = applicant_features.get(
        "NumberOfDependents",
        "Not available"
    )

    home_ownership = applicant_features.get(
        "HomeOwnershipStatus",
        "Not available"
    )

    loan_duration = applicant_features.get(
        "LoanDuration",
        "Not available"
    )

    loan_purpose = applicant_features.get(
        "LoanPurpose",
        "Not available"
    )

    dti_ratio = applicant_features.get(
        "DebtToIncomeRatio",
        0
    )

    previous_defaults = applicant_features.get(
        "PreviousLoanDefaults",
        "Not available"
    )

    bankruptcy_history = applicant_features.get(
        "BankruptcyHistory",
        "Not available"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Age:**", age)

        st.write(
            "**Education Level:**",
            education
        )

        st.write(
            "**Employment Status:**",
            employment_status
        )

        st.write(
            "**Experience:**",
            f"{experience} years"
        )

        st.write(
            "**Job Tenure:**",
            f"{job_tenure} years"
        )

        st.write(
            "**Marital Status:**",
            marital_status
        )

    with col2:

        st.write(
            "**Number of Dependents:**",
            dependents
        )

        st.write(
            "**Home Ownership:**",
            home_ownership
        )

        st.write(
            "**Loan Duration:**",
            f"{loan_duration} months"
        )

        st.write(
            "**Loan Purpose:**",
            loan_purpose
        )

        st.write(
            "**Debt-to-Income Ratio:**",
            f"{dti_ratio:.2f}"
        )

        st.write(
            "**Previous Loan Defaults:**",
            previous_defaults
        )

        st.write(
            "**Bankruptcy History:**",
            bankruptcy_history
        )

    st.divider()

    # =====================================================
    # RISK INTERPRETATION
    # =====================================================

    st.subheader("🔎 Risk Interpretation")

    if risk_level == "Low":

        st.success(
            "The model classified this applicant as "
            "having a low predicted risk."
        )

    elif risk_level == "Medium":

        st.warning(
            "The model classified this applicant as "
            "having a medium predicted risk."
        )

    elif risk_level == "High":

        st.error(
            "The model classified this applicant as "
            "having a high predicted risk."
        )

    else:

        st.info(
            "The risk level returned by the model "
            "could not be interpreted."
        )

    st.caption(
        "This analysis is based on the trained machine "
        "learning model and the submitted applicant data. "
        "It is not a final lending decision."
    )
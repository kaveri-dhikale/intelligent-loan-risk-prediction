import streamlit as st


def show_home():

    # =====================================================
    # HEADER
    # =====================================================

    st.title("Loan Risk Prediction System")

    st.write(
        "Intelligent assessment of loan eligibility and "
        "applicant financial risk using machine learning."
    )

    st.divider()

    # =====================================================
    # OVERVIEW CARDS
    # =====================================================

    st.subheader("System Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="Prediction Engine",
            value="Random Forest"
        )

    with col2:
        st.metric(
            label="Applicant Features",
            value="29"
        )

    with col3:
        st.metric(
            label="Prediction Output",
            value="Risk"
        )

    with col4:
        st.metric(
            label="API Status",
            value="Ready"
        )

    st.divider()

    # =====================================================
    # PROJECT OVERVIEW
    # =====================================================

    st.header("About the System")

    col1, col2 = st.columns([1.5, 1])

    with col1:

        st.subheader("Intelligent Loan Risk Assessment")

        st.write(
            "This system evaluates an applicant's personal, "
            "employment, credit, loan and financial information "
            "to predict loan approval and assess associated "
            "financial risk."
        )

        st.write(
            "The machine learning pipeline preprocesses "
            "applicant information before passing it to a "
            "trained Random Forest model."
        )

        st.write(
            "The prediction service provides both the decision "
            "and probability-based risk information."
        )

    with col2:

        st.subheader("🔐 Data-Driven Assessment")

        st.write(
            "Analyze multiple financial and credit indicators "
            "together instead of relying on a single attribute."
        )

        st.divider()

        st.subheader("📊 Explainable Results")

        st.write(
            "Explore the factors associated with the prediction "
            "through visual analytics and explainability."
        )

    st.divider()

    # =====================================================
    # WORKFLOW
    # =====================================================

    st.header("Machine Learning Workflow")

    workflow = [
        (
            "01",
            "Applicant Data",
            "Enter personal, financial and credit information."
        ),
        (
            "02",
            "Preprocessing",
            "Clean, transform and scale the input data."
        ),
        (
            "03",
            "Feature Selection",
            "Select the features used by the trained model."
        ),
        (
            "04",
            "Prediction",
            "Random Forest generates the loan prediction."
        ),
        (
            "05",
            "Risk Analysis",
            "Display probability and associated risk level."
        )
    ]

    cols = st.columns(5)

    for col, item in zip(cols, workflow):

        number, title, description = item

        with col:

            st.subheader(f"Step {number}")
            st.write(f"**{title}**")
            st.caption(description)

    st.divider()

    # =====================================================
    # TECHNOLOGY STACK
    # =====================================================

    st.header("Technology Stack")

    technologies = [
        ("🎨", "Streamlit", "Frontend"),
        ("⚡", "FastAPI", "Backend API"),
        ("🤖", "Random Forest", "ML Model"),
        ("📊", "Plotly", "Visualization")
    ]

    col1, col2, col3, col4 = st.columns(4)

    for col, technology in zip(
        [col1, col2, col3, col4],
        technologies
    ):

        icon, name, category = technology

        with col:

            st.subheader(f"{icon} {name}")
            st.caption(category)
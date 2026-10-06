
import streamlit as st
import joblib
import os
import pandas as pd
import matplotlib.pyplot as plt


def show_model_performance():

    # ============================================================
    # PAGE TITLE
    # ============================================================

    st.markdown(
        '<div class="page-title">📈 Model Performance</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            color:#9ca3af;
            margin-bottom:25px;
        ">
            Performance evaluation of the Random Forest
            loan approval prediction model.
        </div>
        """,
        unsafe_allow_html=True
    )

    # ============================================================
    # MODEL DIRECTORY
    # ============================================================

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(__file__)
            )
        )
    )

    MODEL_DIR = os.path.join(
        BASE_DIR,
        "models"
    )

    metrics_path = os.path.join(
        MODEL_DIR,
        "model_metrics.pkl"
    )

    config_path = os.path.join(
        MODEL_DIR,
        "model_config.pkl"
    )

    model_path = os.path.join(
        MODEL_DIR,
        "loan_model.pkl"
    )

    # ============================================================
    # CHECK MODEL FILES
    # ============================================================

    if not os.path.exists(metrics_path):

        st.error(
            "❌ model_metrics.pkl not found."
        )

        st.info(
            """
            Please copy model_metrics.pkl from your Colab
            model folder into the project's models folder.
            """
        )

        return

    # ============================================================
    # LOAD METRICS
    # ============================================================

    try:

        metrics = joblib.load(
            metrics_path
        )

    except Exception as error:

        st.error(
            f"Unable to load model metrics: {error}"
        )

        return

    # ============================================================
    # LOAD MODEL CONFIGURATION
    # ============================================================

    config = {}

    if os.path.exists(config_path):

        try:

            config = joblib.load(
                config_path
            )

        except Exception as error:

            st.warning(
                f"Could not load model configuration: {error}"
            )

    # ============================================================
    # MODEL INFORMATION
    # ============================================================

    model_name = config.get(
        "model_name",
        "Random Forest"
    )

    selected_features = config.get(
        "selected_features",
        "N/A"
    )

    target_column = config.get(
        "target_column",
        "LoanApproved"
    )

    # ============================================================
    # TOP INFORMATION CARDS
    # ============================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Algorithm",
            model_name
        )

    with col2:

        st.metric(
            "Problem Type",
            "Binary Classification"
        )

    with col3:

        st.metric(
            "Target",
            target_column
        )

    st.markdown("---")

    # ============================================================
    # PERFORMANCE METRICS
    # ============================================================

    st.subheader("📊 Evaluation Metrics")

    accuracy = metrics.get(
        "accuracy",
        0
    )

    precision = metrics.get(
        "precision",
        0
    )

    recall = metrics.get(
        "recall",
        0
    )

    f1_score = metrics.get(
        "f1_score",
        0
    )

    roc_auc = metrics.get(
        "roc_auc",
        0
    )

    # Convert to percentage

    accuracy_percentage = accuracy * 100
    precision_percentage = precision * 100
    recall_percentage = recall * 100
    f1_percentage = f1_score * 100
    roc_auc_percentage = roc_auc * 100

    # ============================================================
    # METRIC CARDS
    # ============================================================

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:

        st.metric(
            "Accuracy",
            f"{accuracy_percentage:.2f}%"
        )

    with col2:

        st.metric(
            "Precision",
            f"{precision_percentage:.2f}%"
        )

    with col3:

        st.metric(
            "Recall",
            f"{recall_percentage:.2f}%"
        )

    with col4:

        st.metric(
            "F1 Score",
            f"{f1_percentage:.2f}%"
        )

    with col5:

        st.metric(
            "ROC-AUC",
            f"{roc_auc_percentage:.2f}%"
        )

    st.markdown("---")

    # ============================================================
    # PERFORMANCE CHART
    # ============================================================

    st.subheader("📈 Performance Comparison")

    metric_names = [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score",
        "ROC-AUC"
    ]

    metric_values = [
        accuracy_percentage,
        precision_percentage,
        recall_percentage,
        f1_percentage,
        roc_auc_percentage
    ]

    performance_df = pd.DataFrame({

        "Metric": metric_names,

        "Score": metric_values

    })

    fig, ax = plt.subplots(
        figsize=(9, 5)
    )

    ax.bar(
        performance_df["Metric"],
        performance_df["Score"]
    )

    ax.set_ylim(
        0,
        100
    )

    ax.set_ylabel(
        "Score (%)"
    )

    ax.set_title(
        "Random Forest Model Performance"
    )

    # Display values above bars

    for index, value in enumerate(
        performance_df["Score"]
    ):

        ax.text(
            index,
            value + 1,
            f"{value:.2f}%",
            ha="center"
        )

    st.pyplot(
        fig,
        use_container_width=True
    )

    # ============================================================
    # MODEL CONFIGURATION
    # ============================================================

    st.subheader("⚙️ Model Configuration")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "**Algorithm:**",
            model_name
        )

        st.write(
            "**Feature Selection:**",
            "Mutual Information"
        )

        st.write(
            "**Selected Features:**",
            selected_features
        )

    with col2:

        st.write(
            "**Class Balancing:**",
            "Class Weight = Balanced"
        )

        st.write(
            "**Number of Trees:**",
            "200"
        )

        st.write(
            "**Random State:**",
            "42"
        )

    st.markdown("---")

    # ============================================================
    # PERFORMANCE INTERPRETATION
    # ============================================================

    st.subheader("📌 Performance Interpretation")

    if accuracy >= 0.90:

        st.success(
            f"""
            The Random Forest model achieved an accuracy of
            {accuracy_percentage:.2f}%, indicating strong
            predictive performance on the test dataset.
            """
        )

    elif accuracy >= 0.75:

        st.info(
            f"""
            The Random Forest model achieved an accuracy of
            {accuracy_percentage:.2f}%, indicating good
            predictive performance on the test dataset.
            """
        )

    else:

        st.warning(
            f"""
            The Random Forest model achieved an accuracy of
            {accuracy_percentage:.2f}%. Further model tuning
            may improve predictive performance.
            """
        )

    # ============================================================
    # MODEL FILE STATUS
    # ============================================================

    st.subheader("📁 Model Status")

    if os.path.exists(model_path):

        st.success(
            "✓ Random Forest model loaded successfully."
        )

    else:

        st.warning(
            "⚠️ loan_model.pkl not found."
        )

    st.markdown("---")

    st.caption(
        "LoanRisk AI • Random Forest Credit Risk Prediction System"
    )


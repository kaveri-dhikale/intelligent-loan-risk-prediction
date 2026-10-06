
import os
import joblib
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


def show_explainability():

    # ---------------------------------------------------------
    # PAGE TITLE
    # ---------------------------------------------------------

    st.title("🔍 Model Explainability")
    st.caption(
        "Understand which factors influence the Random Forest loan approval prediction."
    )

    # ---------------------------------------------------------
    # MODEL PATH
    # ---------------------------------------------------------

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )
    )

    MODEL_DIR = os.path.join(BASE_DIR, "models")

    model_path = os.path.join(MODEL_DIR, "loan_model.pkl")
    preprocessor_path = os.path.join(MODEL_DIR, "preprocessor.pkl")
    selector_path = os.path.join(MODEL_DIR, "feature_selector.pkl")
    config_path = os.path.join(MODEL_DIR, "model_config.pkl")

    # ---------------------------------------------------------
    # CHECK FILES
    # ---------------------------------------------------------

    required_files = [
        model_path,
        preprocessor_path,
        selector_path
    ]

    missing_files = [
        file for file in required_files
        if not os.path.exists(file)
    ]

    if missing_files:
        st.error("Required model files are missing.")

        for file in missing_files:
            st.write(f"❌ {file}")

        return

    # ---------------------------------------------------------
    # LOAD MODEL
    # ---------------------------------------------------------

    try:

        model = joblib.load(model_path)
        preprocessor = joblib.load(preprocessor_path)
        feature_selector = joblib.load(selector_path)

        config = {}

        if os.path.exists(config_path):
            config = joblib.load(config_path)

    except Exception as e:

        st.error("Unable to load model files.")
        st.exception(e)

        return

    # ---------------------------------------------------------
    # MODEL INFORMATION
    # ---------------------------------------------------------

    st.subheader("🤖 Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Model",
            config.get("model_name", "Random Forest")
        )

    with col2:
        st.metric(
            "Trees",
            "200"
        )

    with col3:
        st.metric(
            "Feature Selection",
            "Mutual Information"
        )

    # ---------------------------------------------------------
    # FEATURE NAMES
    # ---------------------------------------------------------

    try:

        # Get all transformed feature names
        feature_names = preprocessor.get_feature_names_out()

        # Get selected features from SelectKBest
        selected_mask = feature_selector.get_support()

        selected_feature_names = feature_names[selected_mask]

        # Get Random Forest importance
        importances = model.feature_importances_

        # Safety check
        if len(selected_feature_names) != len(importances):

            st.warning(
                "Feature names and model importance values do not match."
            )

            return

        importance_df = pd.DataFrame({
            "Feature": selected_feature_names,
            "Importance": importances
        })

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )

    except Exception as e:

        st.error("Unable to calculate feature importance.")
        st.exception(e)

        return

    # ---------------------------------------------------------
    # TOP FEATURES
    # ---------------------------------------------------------

    st.subheader("📊 Top Factors Influencing Loan Approval")

    top_n = min(10, len(importance_df))

    top_features = importance_df.head(top_n).copy()

    # Clean feature names
    top_features["Feature"] = (
        top_features["Feature"]
        .str.replace("num__", "", regex=False)
        .str.replace("cat__", "", regex=False)
    )

    # Display table
    display_df = top_features.copy()

    display_df["Importance"] = (
        display_df["Importance"] * 100
    ).round(2)

    display_df = display_df.rename(
        columns={
            "Feature": "Feature",
            "Importance": "Importance (%)"
        }
    )

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    # ---------------------------------------------------------
    # FEATURE IMPORTANCE CHART
    # ---------------------------------------------------------

    st.subheader("📈 Feature Importance")

    chart_df = top_features.sort_values(
        by="Importance",
        ascending=True
    )

    fig, ax = plt.subplots(figsize=(9, 5))

    ax.barh(
        chart_df["Feature"],
        chart_df["Importance"]
    )

    ax.set_xlabel("Importance")
    ax.set_ylabel("Feature")

    ax.set_title(
        "Top Features Used by Random Forest"
    )

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)

    # ---------------------------------------------------------
    # EXPLANATION
    # ---------------------------------------------------------

    st.subheader("🧠 How the Model Makes Decisions")

    st.info(
        """
        The Random Forest model analyzes multiple applicant characteristics
        and combines the predictions of 200 decision trees.

        Before prediction, the input data is processed using the preprocessing
        pipeline. Mutual Information SelectKBest then selects the most
        informative features.

        The Random Forest uses these selected features to determine whether
        the loan should be classified as Approved or Rejected.
        """
    )

    # ---------------------------------------------------------
    # IMPORTANT NOTE
    # ---------------------------------------------------------

    st.subheader("💡 Understanding Feature Importance")

    st.write(
        """
        Feature importance indicates how useful a feature was to the Random
        Forest when making its decisions.

        A higher importance value means that the feature contributed more to
        the model's overall decision-making process.

        However, feature importance does not mean that the feature always
        increases loan approval. It only indicates its relative importance
        to the model.
        """
    )

    # ---------------------------------------------------------
    # SELECTED FEATURES
    # ---------------------------------------------------------

    with st.expander("📋 View Selected Features"):

        clean_features = [
            feature
            .replace("num__", "")
            .replace("cat__", "")
            for feature in selected_feature_names
        ]

        for i, feature in enumerate(clean_features, start=1):

            st.write(
                f"**{i}.** {feature}"
            )

    # ---------------------------------------------------------
    # MODEL PIPELINE
    # ---------------------------------------------------------

    with st.expander("⚙️ View Model Pipeline"):

        st.markdown(
            """
            **Input Applicant Data**

            ↓

            **Missing Value Handling**

            ↓

            **Numerical Feature Scaling**

            ↓

            **Categorical Feature Encoding**

            ↓

            **Mutual Information Feature Selection**

            ↓

            **Random Forest Classifier**

            ↓

            **Loan Approval Prediction**
            """
        )

    # ---------------------------------------------------------
    # FOOTER
    # ---------------------------------------------------------

    st.divider()

    st.caption(
        "Explainability module • Random Forest • Mutual Information Feature Selection"
    )







import streamlit as st

from components.styles import load_css
from components.sidebar import render_sidebar

from pages.home import show_home
from pages.prediction import show_prediction
from pages.risk_analysis import show_risk_analysis
from pages.model_performance import show_model_performance
from pages.explainability import show_explainability
# PAGE CONFIGURATION

st.set_page_config(
    page_title="LoanRisk AI",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)


# GLOBAL STYLES

load_css()


# SIDEBAR

page = render_sidebar()




# =====================================================
# PAGE ROUTING
# =====================================================

if page == "🏠 Overview":

    show_home()


elif page == "📝 Loan Prediction":

    show_prediction()


elif page == "📊 Risk Analysis":
    show_risk_analysis()


elif page == "📈 Model Performance":

    show_model_performance()

elif page == "🔍 Explainability":
    show_explainability()
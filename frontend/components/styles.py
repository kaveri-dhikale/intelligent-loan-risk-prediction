# import streamlit as st


# def load_css():

#     st.markdown(
#         """
#         <style>

#         /* =====================================================
#            GLOBAL
#         ===================================================== */

#         .stApp {
#             background-color: #f6f8fb;
#         }

#         .main .block-container {
#             padding-top: 2rem;
#             padding-bottom: 3rem;
#             max-width: 1450px;
#         }

#         /* Hide Streamlit default elements */

#         #MainMenu {
#             visibility: hidden;
#         }

#         footer {
#             visibility: hidden;
#         }

#         header {
#             background: transparent !important;
#         }


#         /* =====================================================
#            SIDEBAR
#         ===================================================== */

#         section[data-testid="stSidebar"] {
#             background-color: #111827;
#             border-right: 1px solid #1f2937;
#         }

#         section[data-testid="stSidebar"] * {
#             color: #f9fafb;
#         }

#         section[data-testid="stSidebar"] .stRadio label {
#             padding: 8px 10px;
#             border-radius: 8px;
#         }


#         /* =====================================================
#            PAGE HEADER
#            ===================================================== */

#         .page-title {
#             font-size: 34px;
#             font-weight: 700;
#             color: #111827;
#             margin-bottom: 4px;
#         }

#         .page-subtitle {
#             font-size: 15px;
#             color: #6b7280;
#             margin-bottom: 28px;
#         }


#         /* =====================================================
#            BRAND
#            ===================================================== */

#         .brand-title {
#             font-size: 23px;
#             font-weight: 700;
#             color: #ffffff;
#             margin-bottom: 2px;
#         }

#         .brand-subtitle {
#             font-size: 12px;
#             color: #9ca3af;
#             margin-bottom: 25px;
#         }


#         /* =====================================================
#            CARDS
#            ===================================================== */

#         .dashboard-card {
#             background: #ffffff;
#             border: 1px solid #e5e7eb;
#             border-radius: 14px;
#             padding: 22px;
#             min-height: 140px;
#             box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
#         }

#         .card-label {
#             font-size: 13px;
#             color: #6b7280;
#             margin-bottom: 8px;
#         }

#         .card-value {
#             font-size: 27px;
#             font-weight: 700;
#             color: #111827;
#         }

#         .card-description {
#             font-size: 12px;
#             color: #9ca3af;
#             margin-top: 8px;
#         }


#         /* =====================================================
#            FEATURE CARDS
#            ===================================================== */

#         .feature-card {
#             background: #ffffff;
#             border: 1px solid #e5e7eb;
#             border-radius: 14px;
#             padding: 24px;
#             min-height: 175px;
#             box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
#         }

#         .feature-icon {
#             font-size: 28px;
#             margin-bottom: 12px;
#         }

#         .feature-title {
#             font-size: 17px;
#             font-weight: 650;
#             color: #111827;
#             margin-bottom: 8px;
#         }

#         .feature-text {
#             font-size: 13px;
#             line-height: 1.6;
#             color: #6b7280;
#         }


#         /* =====================================================
#            SECTION TITLE
#            ===================================================== */

#         .section-title {
#             font-size: 21px;
#             font-weight: 650;
#             color: #111827;
#             margin-top: 30px;
#             margin-bottom: 14px;
#         }


#         /* =====================================================
#            WORKFLOW
#            ===================================================== */

#         .workflow-card {
#             background: #ffffff;
#             border: 1px solid #e5e7eb;
#             border-radius: 14px;
#             padding: 20px;
#             text-align: center;
#             min-height: 130px;
#         }

#         .workflow-number {
#             font-size: 12px;
#             color: #6b7280;
#             margin-bottom: 7px;
#         }

#         .workflow-title {
#             font-size: 15px;
#             font-weight: 650;
#             color: #111827;
#         }

#         .workflow-description {
#             font-size: 12px;
#             color: #6b7280;
#             margin-top: 5px;
#         }


#         /* =====================================================
#            BUTTONS
#            ===================================================== */

#         .stButton > button {
#             border-radius: 9px;
#             border: none;
#             font-weight: 600;
#             padding: 0.55rem 1.2rem;
#         }


#         /* =====================================================
#            INPUTS
#            ===================================================== */

#         div[data-baseweb="input"] {
#             border-radius: 8px;
#         }

#         div[data-baseweb="select"] {
#             border-radius: 8px;
#         }


#         /* =====================================================
#            DIVIDER
#            ===================================================== */

#         .custom-divider {
#             height: 1px;
#             background: #e5e7eb;
#             margin: 24px 0;
#         }

#         </style>
#         """,
#         unsafe_allow_html=True
#     )










































































# import streamlit as st


# def load_css():
#     st.markdown(
#         """
#         <style>

#         /* Main application */
#         .stApp {
#             background-color: #f6f8fb;
#         }

#         .main .block-container {
#             max-width: 1450px;
#             padding-top: 2rem;
#             padding-bottom: 2rem;
#         }

#         /* Hide Streamlit branding */
#         #MainMenu {
#             visibility: hidden;
#         }

#         footer {
#             visibility: hidden;
#         }

#         /* Sidebar */
#         section[data-testid="stSidebar"] {
#             background-color: #111827;
#         }

#         section[data-testid="stSidebar"] * {
#             color: white;
#         }

#         /* Page title */
#         .page-title {
#             font-size: 36px;
#             font-weight: 700;
#             margin-bottom: 5px;
#             color: #111827;
#         }

#         .page-subtitle {
#             font-size: 16px;
#             color: #6b7280;
#             margin-bottom: 30px;
#         }

#         /* Brand */
#         .brand-title {
#             font-size: 24px;
#             font-weight: 700;
#             color: white;
#         }

#         .brand-subtitle {
#             font-size: 13px;
#             color: #9ca3af;
#         }

#         /* Cards */
#         .dashboard-card {
#             background: white;
#             padding: 22px;
#             border-radius: 14px;
#             border: 1px solid #e5e7eb;
#             margin-bottom: 20px;
#         }

#         .feature-card {
#             background: white;
#             padding: 20px;
#             border-radius: 14px;
#             border: 1px solid #e5e7eb;
#         }

#         .section-title {
#             font-size: 22px;
#             font-weight: 700;
#             color: #111827;
#             margin-top: 20px;
#             margin-bottom: 10px;
#         }

#         .workflow-card {
#             background: white;
#             padding: 18px;
#             border-radius: 12px;
#             border: 1px solid #e5e7eb;
#             text-align: center;
#         }

#         /* Buttons */
#         .stButton > button {
#             width: 100%;
#             border-radius: 10px;
#             padding: 0.65rem 1rem;
#             font-weight: 600;
#         }

#         /* Divider */
#         .divider {
#             height: 1px;
#             background-color: #e5e7eb;
#             margin: 25px 0;
#         }

#         </style>
#         """,
#         unsafe_allow_html=True
#     )

import streamlit as st


def load_css():
    pass
# import streamlit as st


# def render_sidebar():

#     with st.sidebar:

#         # -------------------------------------------------
#         # BRAND
#         # -------------------------------------------------

#         st.markdown(
#             """
#             <div class="brand-title">
#                 💳 LoanRisk AI
#             </div>

#             <div class="brand-subtitle">
#                 Intelligent Credit Risk Platform
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         st.markdown("---")

#         # -------------------------------------------------
#         # NAVIGATION
#         # -------------------------------------------------

#         st.markdown(
#             """
#             <div style="
#                 font-size:12px;
#                 color:#9ca3af;
#                 margin-bottom:8px;
#                 text-transform:uppercase;
#                 letter-spacing:0.5px;
#             ">
#                 Navigation
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         page = st.radio(
#             "Navigation",
#             [
#                 "🏠 Overview",
#                 "📝 Loan Prediction",
#                 "📊 Risk Analysis",
#                 "📈 Model Performance",
#                 "🔍 Explainability"
#             ],
#             label_visibility="collapsed"
#         )

#         st.markdown("---")

#         # -------------------------------------------------
#         # SYSTEM STATUS
#         # -------------------------------------------------

#         st.markdown(
#             """
#             <div style="
#                 background:#1f2937;
#                 border-radius:10px;
#                 padding:12px;
#                 margin-top:10px;
#             ">
#                 <div style="
#                     font-size:12px;
#                     color:#9ca3af;
#                 ">
#                     SYSTEM STATUS
#                 </div>

#                 <div style="
#                     margin-top:7px;
#                     font-size:13px;
#                     color:#d1fae5;
#                 ">
#                     ● Ready
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True
#         )

#         st.markdown("")

#         st.caption("Loan Risk Prediction System")
#         st.caption("Machine Learning Application")

#     return page

































import streamlit as st


def render_sidebar():

    with st.sidebar:

        # ============================================
        # BRAND
        # ============================================

        st.markdown(
            """
            <div style="
                font-size:24px;
                font-weight:700;
                margin-bottom:3px;
            ">
                💳 LoanRisk AI
            </div>

            <div style="
                font-size:12px;
                color:#9ca3af;
                margin-bottom:15px;
            ">
                Credit Risk Prediction
            </div>
            """,
            unsafe_allow_html=True
        )

        # ============================================
        # NAVIGATION
        # ============================================

        page = st.radio(
            "Navigation",
            [
                "🏠 Overview",
                "📝 Loan Prediction",
                "📊 Risk Analysis",
                "📈 Model Performance",
                "🔍 Explainability"
            ],
            label_visibility="collapsed"
        )

        # ============================================
        # SYSTEM STATUS
        # ============================================

        st.markdown(
            """
            <div style="
                margin-top:25px;
                padding:10px;
                border-radius:8px;
                background:#1f2937;
                font-size:12px;
            ">
                <span style="color:#86efac;">●</span>
                <span style="color:#d1d5db;">
                    System Ready
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

    return page


import streamlit as st

# Set page layout and style
st.set_page_config(page_title="Welcome to CSI Analysis", page_icon="📊", layout="wide")

# Apply a clean, minimal style for the app
st.markdown("""
    <style>
    .css-1d391kg {font-family: 'Roboto', sans-serif;}
    .stSelectbox, .stButton, .stTextInput {font-size: 16px;}
    .stMarkdown {padding-top: 0.8rem; padding-bottom: 1.2rem;}
    .css-ffhzg2 {background-color: #f0f4f8;}
    </style>
""", unsafe_allow_html=True)

# --- Welcome Page ---
def show_welcome_page():
    # Title section
    st.markdown("<h1 style='text-align: center;'>Welcome to CSI Analysis 2024/2025</h1>", unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>(TATA Commercial, MB, Agri Service)</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <p style='text-align: center;'>This platform provides an integrated toolset for analyzing Customer Satisfaction Index (CSI) data for multiple brands.
    Explore insights into customer satisfaction, performance metrics, and predictive modeling across various sectors, including automotive and agriculture.</p>
    """, unsafe_allow_html=True)
    
    # Analysis Breakdown (general for all brands)
    st.markdown("### Key Functionalities for Analysis")
    st.markdown("""
    1. **Data Selection**: Choose your dataset and brand for analysis.
    2. **Correlation Analysis**: View the relationships between various satisfaction factors.
    3. **Performance Metrics**: Evaluate customer satisfaction performance for each brand.
    4. **Predictive Analysis**: Understand future trends in customer satisfaction.
    5. **Visual Insights**: Interactive plots to visualize correlation and importance metrics.
    """, unsafe_allow_html=True)
    

    # Add copyright footer
    st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #071429;
        color: #b4b8bf;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        © 2025 DIMO Customer Experience. All rights reserved.
    </div>
    """, unsafe_allow_html=True)

# Show the welcome page
show_welcome_page()

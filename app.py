import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="LoanPredict AI",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("loan_model.pkl")

# ---------------- CSS ----------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    text-align: center;
    margin-bottom: 20px;
}

.result-approved {
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 2px solid #28a745;
    margin-top: 20px;
}

.result-rejected {
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    border: 2px solid #dc3545;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOGIN STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown(
        '<div class="main-title">🏦 LoanPredict AI</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Loan Approval Prediction System Using Machine Learning</div>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("🚀 Login", use_container_width=True):

            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("❌ Invalid Username or Password")

        st.caption("Demo Login: admin / 1234")

    st.stop()

# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.title("🏦 LoanPredict AI")
    st.caption("Loan Approval Prediction System")

    st.divider()

    st.subheader("📖 About Project")

    st.write(
        "LoanPredict AI is a Machine Learning based system "
        "that predicts whether a loan application is likely "
        "to be approved or rejected."
    )

    st.write("🤖 **Model:** Random Forest")
    st.write("🎯 **Accuracy:** 97.78%")
    st.write("📊 **Prediction:** Loan Approval")

    st.divider()

    st.subheader("⚙️ Features")

    st.write("• Applicant information")
    st.write("• CIBIL score analysis")
    st.write("• Asset details")
    st.write("• Loan amount and term")
    st.write("• Instant prediction")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

# ---------------- MAIN DASHBOARD ----------------

st.markdown(
    '<div class="main-title">Loan Approval Prediction Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-powered loan application analysis</div>',
    unsafe_allow_html=True
)

# ---------------- DASHBOARD CARDS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🤖 ML Model</h3>
        <p>Random Forest</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🎯 Accuracy</h3>
        <p>97.78%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>🏦 System</h3>
        <p>Loan Approval</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------- APPLICANT DETAILS ----------------

st.header("👤 Applicant Details")

col1, col2 = st.columns(2)

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=20,
        value=2
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    income_annum = st.number_input(
        "Annual Income (₹)",
        min_value=0,
        value=500000,
        step=10000
    )

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        min_value=0,
        value=1000000,
        step=10000
    )

    loan_term = st.number_input(
        "Loan Term (Years)",
        min_value=1,
        max_value=50,
        value=10
    )

with col2:

    cibil_score = st.number_input(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=700
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value (₹)",
        min_value=0,
        value=1000000,
        step=10000
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value (₹)",
        min_value=0,
        value=500000,
        step=10000
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value (₹)",
        min_value=0,
        value=500000,
        step=10000
    )

    bank_asset_value = st.number_input(
        "Bank Asset Value (₹)",
        min_value=0,
        value=500000,
        step=10000
    )

# ---------------- ENCODING ----------------

education_value = 0 if education == "Graduate" else 1
self_employed_value = 0 if self_employed == "No" else 1

# ---------------- INPUT DATA ----------------

input_data = pd.DataFrame({
    "no_of_dependents": [no_of_dependents],
    "education": [education_value],
    "self_employed": [self_employed_value],
    "income_annum": [income_annum],
    "loan_amount": [loan_amount],
    "loan_term": [loan_term],
    "cibil_score": [cibil_score],
    "residential_assets_value": [residential_assets_value],
    "commercial_assets_value": [commercial_assets_value],
    "luxury_assets_value": [luxury_assets_value],
    "bank_asset_value": [bank_asset_value]
})

# ---------------- PREDICTION ----------------

st.divider()

if st.button("🔍 Predict Loan Approval", use_container_width=True):

    prediction = model.predict(input_data)[0]

    # Income rule
    if income_annum < 100000:

        st.markdown("""
        <div class="result-rejected">
            <h2>❌ Loan Rejected</h2>
            <p>Annual income is below ₹1,00,000.</p>
        </div>
        """, unsafe_allow_html=True)

    elif prediction == 0:

        st.markdown("""
        <div class="result-approved">
            <h2>🎉 Loan Approved</h2>
            <p>The Machine Learning model predicts that the loan application is likely to be approved.</p>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-rejected">
            <h2>❌ Loan Rejected</h2>
            <p>The Machine Learning model predicts that the loan application is likely to be rejected.</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

st.caption("LoanPredict AI | Machine Learning Based Loan Approval Prediction System")

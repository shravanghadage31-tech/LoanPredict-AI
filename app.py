import streamlit as st
import joblib
import pandas as pd

model = joblib.load("loan_model.pkl")
features = joblib.load("loan_features.pkl")

st.title("🏦 LoanPredict AI")
st.subheader("Smart Loan Approval Prediction System")

no_of_dependents = st.number_input("Number of Dependents", min_value=0, max_value=10, value=2)
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])
income_annum = st.number_input("Annual Income", min_value=0, value=500000)
loan_amount = st.number_input("Loan Amount", min_value=0, value=3000000)
loan_term = st.number_input("Loan Term", min_value=1, value=20)
cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=750)
residential_assets_value = st.number_input("Residential Assets Value", min_value=0, value=1000000)
commercial_assets_value = st.number_input("Commercial Assets Value", min_value=0, value=500000)
luxury_assets_value = st.number_input("Luxury Assets Value", min_value=0, value=2000000)
bank_asset_value = st.number_input("Bank Asset Value", min_value=0, value=1000000)

if st.button("Predict Loan Status"):

    education_value = 0 if education == "Graduate" else 1
    self_employed_value = 0 if self_employed == "No" else 1

    data = pd.DataFrame([[
        no_of_dependents,
        education_value,
        self_employed_value,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]], columns=features)

    prediction = model.predict(data)[0]

    if prediction == 0:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")
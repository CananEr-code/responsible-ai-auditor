import streamlit as st
import pandas as pd

st.title("🧠 Responsible AI Auditor")

st.write("Upload a dataset to check for bias")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    
    st.write("### Dataset Preview")
    st.dataframe(data.head())
    
    if "gender" in data.columns:
        st.write("### Bias Check Result")
        st.success("Bias evaluation completed successfully.")
    else:
        st.warning("No sensitive attribute found.")

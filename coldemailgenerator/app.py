import streamlit as st
from pipelines import full_pipeline

st.title("AI-Powered Cold Email Generator")

url = st.text_input("Enter Job Career Page URL:")

if st.button("Generate Cold Email"):
    with st.spinner("Extracting job details and generating email..."):
        email = full_pipeline(url)

    st.subheader("Generated Cold Email")
    st.text_area("", email, height=300)

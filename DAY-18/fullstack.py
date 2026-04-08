import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration

st.set_page_config(page_title="Single -page Multiple Navigations",layout="wide")

# Side Bar Navigation
st.sidebar.title("Navigation")
page=st.sidebar.radio("Go To",["🏡Home","📄About","📊Chart","📞Contact"])

# Home Page
if page=="🏡Home":
    st.title("🏡Home Page")
    st.write("Welcome to Home page")
    st.success("Use to the slide bars to explore our pages")

# About page
elif page=="📄About":
    st.title("Welcome to About Page📄")
    st.success("User Information")
    st.markdown("""
                This is first Streamlit page
                If you want to explore the pages go to sidebar Navigation
                Welcome
                """)
    
# Chart Page
elif page=="📊Chart":
    st.title("Charts Page")
    st.subheader("Random Data chart")
    data=pd.DataFrame(np.random.randn(20,3), columns=["A","B","C"])
    st.line_chart(data)
    st.subheader("Area Chart")
    st.area_chart(data)
    st.subheader("data table")
    st.table(data.head())

# Contact Page
elif page=="📞Contact":
    st.title("Contact Details📞")

    with st.form("ContactInformation"):
        name = st.text_input("Name")
        email=st.text_input("Email ID")
        messages=st.text_area("Message")
        submit=st.form_submit_button("Send")
        
        if submit:
            st.success(f"Thank you {name}, We have received your message")
import streamlit as st
st.title("Hello!")
st.write("Welcome to my First Streamlit Web Application")
st.text_input("filed")
st.balloons()
st.snow()
name = st.text_input("enter ur name")
if st.button("click button"):
    st.success(f"Hello!, {name}")

st.line_chart([3,5,7])
st.bar_chart([3,4,7])
st.slider("age",0,100)
if st.button("Celebrate!"):
    st.balloons()
    st.snow()

st.checkbox("Happy")

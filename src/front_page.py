import streamlit as st

st.title("Student Grades Homework Application")

st.header('Index')

st.subheader('Query')
st.text('Query: Allow a user to select pre-made queries from our student collection')

st.subheader('viz')
st.text('viz: Queries the mongo DB environment to grab our collection and convert it into a data frame and plot the data into a histogram')

st.subheader("Summary")
st.text('Summary page explaining all the inner workings of the app and the "why" behind each decision made')
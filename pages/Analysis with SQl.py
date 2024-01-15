import streamlit as st


conn = st.connection('mysql', type='sql')
st.write("Python with SQL analysis")



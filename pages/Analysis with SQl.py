import streamlit as st
from mysql.connector import * 

conn = st.connection('mysql', type='sql')
try:

    st.write(conn)
    db_name = st.text_input("enter database name ")
    if st.button("Create Database"):
        sql = "create database " +db_name
        conn._instance.execute(sql)
        st.write("database created")

except Exception as e:
	st.write("issue ", e)

st.write("python with sql anlysis")



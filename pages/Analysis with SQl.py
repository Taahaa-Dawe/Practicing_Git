import streamlit as st
from mysql.connector import * 
conn = st.connection('mysql', type='sql')
try:

    st.write(conn)
    db_name = st.text_input("enter database name ")
    if st.button("Create Database"):
        sql = "create database " +db_name
        conn.execute(sql)
        st.write("database created")

except Exception as e:
	st.write("issue ", e)
finally:
	if con is not None:
		con.close()
print("will analysis with sql")

st.write("python with sql anlysis")


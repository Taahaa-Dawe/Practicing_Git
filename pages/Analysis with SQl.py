import streamlit as st
from mysql.connector import * 
from pages.Sql.mysqlpassword import con

try:

    st.write(con)
    cursor  = con.cursor()
    db_name = st.text_input("enter database name ")
    if st.button("Create Database"):
        sql = "create database " +db_name
        cursor.execute(sql)
    st.write("database created")

except Exception as e:
	st.write("issue ", e)
finally:
	if con is not None:
		con.close()
print("will analysis with sql")

st.write("python with sql anlysis")


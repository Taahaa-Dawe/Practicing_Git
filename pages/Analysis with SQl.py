import streamlit as st
conn = st.sql('mysql'')
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
	if conn is not None:
		conn.close()
print("will analysis with sql")

st.write("python with sql anlysis")


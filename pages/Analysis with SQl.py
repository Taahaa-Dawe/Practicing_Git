import streamlit as st


st.write("DB username:", st.secrets.connections.mysql.host)


# Initialize connection.
conn = st.connection('mysql', type='sql')


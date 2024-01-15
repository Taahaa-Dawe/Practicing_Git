import streamlit as st
from sqlalchemy import create_engine

# Connect to the database
engine = create_engine("mysql+mysqlconnector://root:abc123@localhost:3306")

try:
    st.write(engine)
    
    db_name = st.text_input("Enter database name ")
    
    if st.button("Create Database"):
        # Create the database
        with engine.connect() as connection:
            connection.execute(f"CREATE DATABASE {db_name}")
        st.write("Database created")

except Exception as e:
    st.write("Issue: ", e)

st.write("Python with SQL analysis")



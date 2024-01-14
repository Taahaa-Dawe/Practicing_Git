import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
html_file = open("tp.html", 'r', encoding='UTF-8')
source_code = html_file.read()
html_file.close()

# Read the image file
image_file = open('phototaahaa.jpg', "rb")
contents = image_file.read()
data_url = base64.b64encode(contents).decode("utf-8")
image_file.close()


source_code_with_image = source_code.replace('{data_url}', data_url)

components.html(source_code_with_image, height=2000)
import streamlit as st

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">BioMedical AI app</p>'
st.markdown(new_title, unsafe_allow_html=True)

#st.title("BioMedical AI app")

import subprocess
aaa = subprocess.Popen(["gradio", "app.py"])

gradio_interface_url="http://127.0.0.1:7860/"

st.write(f'<iframe src="{gradio_interface_url}" width="800" height="600"></iframe>',unsafe_allow_html=True)
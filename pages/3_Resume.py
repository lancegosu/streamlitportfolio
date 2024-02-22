import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("Resume")

st.sidebar.header('Project Links')
st.sidebar.markdown('[SpotOn](https://spoton.streamlit.app/)')
st.sidebar.markdown('[Qdoc](https://qdocst.streamlit.app/)')
st.sidebar.markdown('[CooPA](https://coopas.streamlit.app/)')

st.sidebar.header('Contact Info')
st.sidebar.markdown("[Email](mailto:lancemnguyen@gmail.com)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/lancedin)")
st.sidebar.markdown("[Github](https://github.com/lancegosu)")

pdf_viewer(input="../images/resume.pdf", width=900, height=1200)

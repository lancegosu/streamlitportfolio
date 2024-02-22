import streamlit as st
import base64

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

with open("/images/resume.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="900" height="1150" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

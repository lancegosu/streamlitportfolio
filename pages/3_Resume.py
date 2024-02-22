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

with open("images/resume.pdf", "rb") as f:
    base64_pdf = base64.b64encode(f.read()).decode("utf-8")
    
    # Embedding PDF in HTML
    pdf_display = f"""<iframe
        class="pdfobject"
        type="application/pdf"
        title="Embedded PDF"
        src="data:application/pdf;base64,{base64_pdf}"
        style="overflow: auto; width: 100%; height: 100%;"></iframe>"""

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)

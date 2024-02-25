import streamlit as st
import requests
from streamlit_lottie import st_lottie
import base64

st.set_page_config(page_title="Lance's Portfolio")
st.title("👋 Hello world! I'm Lance.")


def add_logo():
    with open("images/profile-pic.png", "rb") as img:
        pic = img.read()
    base64_string = base64.b64encode(pic).decode("utf-8")
    logo = f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: url("data:image/png;base64,{base64_string}");
                background-repeat: no-repeat;
                background-position: 50% 10%;
                margin-top: 10%;
                background-size: 60%;
                padding-top: 150px;
            }}
        </style>
    """
    st.markdown(logo, unsafe_allow_html=True)


add_logo()

st.sidebar.header('Project Links')
st.sidebar.caption('[LLM Optimization with RAG](https://lcrags.streamlit.app/)')
st.sidebar.caption('[SpotOn](https://spoton.streamlit.app/)')
st.sidebar.caption('[Qdoc](https://qdocst.streamlit.app/)')
st.sidebar.caption('[CooPA](https://coopas.streamlit.app/)')

st.sidebar.header('Contact Info')
st.sidebar.caption("[Email](mailto:lancemnguyen@gmail.com)")
st.sidebar.caption("[LinkedIn](https://linkedin.com/in/lancedin)")
st.sidebar.caption("[Github](https://github.com/lancegosu)")

with open("images/resume.pdf", "rb") as pdf:
    resume = pdf.read()

st.sidebar.download_button(label="Download Resume",
                           data=resume,
                           file_name="Lance-Nguyen-Resume.pdf",
                           mime='application/octet-stream')


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_python = load_lottieurl("https://lottie.host/5d248536-e50a-4271-8e23-3a187b6f8d97/pzkssIZZ84.json")
lottie_js = load_lottieurl("https://lottie.host/480a834b-6bd6-466f-a735-867c7dc3edb3/vlX1fIBEEs.json")
lottie_html = load_lottieurl("https://lottie.host/1253a0ad-986e-46bb-b4dc-b597eb5333c7/jCWHwoyFPx.json")
lottie_css = load_lottieurl("https://lottie.host/bb426cc8-e5ef-4f2a-8121-80fae8902d43/ce5uvQHdVP.json")

st.write("Welcome to my portfolio website! Explore the sidebar to learn a little bit about me, my personal projects, and the resources I have used to study AI.")

left, right = st.columns(2)
with left:
    st.image("images/tennis.jpg", caption="Mastery of tennis")
with right:
    st.image("images/niagarafalls.jpg", caption="Niagara Falls, taken in August 2023")

# Skills
st.subheader('⚒️ Skills')
st.write('**Languages**')
col1, col2, col3, col4 = st.columns(4)
with col1:
    st_lottie(lottie_python, height=70, width=70, key="python")
    st.markdown("Python")
with col2:
    st_lottie(lottie_js, height=70, width=70, key="js")
    st.markdown("JavaScript")
with col3:
    st_lottie(lottie_html, height=70, width=70, key="html")
    st.markdown("HTML")
with col4:
    st_lottie(lottie_css, height=70, width=70, key="css")
    st.markdown("CSS")

st.write("**Tools & Frameworks**")
col5, col6, col7, col8 = st.columns(4)
with col5:
    st.markdown("RAG")
    st.markdown("Git")
    st.markdown("AWS EC2")
with col6:
    st.markdown("Prompt Engineering")
    st.markdown("Django")
    st.markdown("AWS S3")
with col7:
    st.markdown("LangChain")
    st.markdown("Flask")
    st.markdown("AWS DynamoDB")
with col8:
    st.markdown("LlamaIndex")
    st.markdown("PyTorch")
    st.markdown("LLMs")

# Education
st.subheader('📚 Education')
col9, col10 = st.columns(2)
with col9:
    st.markdown("""
    **San Jose State University**, *Bachelor of Science in Kinesiology*
    - Dean’s Scholar Award
    - Captain of Club Tennis Team
    """)
with col10:
    st.image("images/spartan.png", width=120)
st.caption('Go Spartans!')

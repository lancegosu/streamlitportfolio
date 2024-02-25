import streamlit as st

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("About Me")

st.sidebar.header('Project Links')
st.sidebar.markdown('[RAG with LangChain](https://lcrags.streamlit.app/)')
st.sidebar.markdown('[SpotOn](https://spoton.streamlit.app/)')
st.sidebar.markdown('[Qdoc](https://qdocst.streamlit.app/)')
st.sidebar.markdown('[CooPA](https://coopas.streamlit.app/)')

st.sidebar.header('Contact Info')
st.sidebar.markdown("[Email](mailto:lancemnguyen@gmail.com)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/lancedin)")
st.sidebar.markdown("[Github](https://github.com/lancegosu)")

with open("images/resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.sidebar.download_button(label="Download Resume",
                           data=PDFbyte,
                           file_name="Lance-Nguyen-Resume.pdf",
                           mime='application/octet-stream')

left, right = st.columns(2)
with left:
    st.header("Where I'm From")
    st.write("""
    I was born and raised in California, a place blessed with some of the most beautiful weather on the planet. 
    Growing up in the Golden State fueled my passion for exploration, be it the bustling city life or the tranquility of 
    the redwood forests. This unique blend of experiences has not only shaped my appreciation for diversity but also 
    influences the creativity I bring to my work as a developer. From the Pacific shores to the tech hubs, California is 
    more than my home; it's a constant source of inspiration. 🌞🌴
    """)
    
    st.header("What I Do Now")
    st.write("""
    Currently, I'm immersed in the world of software development, transforming ideas into vibrant tech solutions. 
    Whether it's crafting sleek websites, optimizing code for AI magic, or diving into the latest tech trends, 
    I'm all about making the digital realm exciting and user-friendly. Let's build something extraordinary together!
    """)
    
    st.header("What I Used to Do")
    st.write("""
    In my past life, I spent over 8 years as a professional tennis coach, shaping the game and personal development of 
    more than 600 students. From empowering beginners to refining strategies for national-level players, each lesson was a 
    unique journey. Transitioning into software engineering, I carry the adaptability and personalized touch from the 
    tennis court into the world of coding, creating tech solutions with a human touch. 🎾💻
    """)

with right:
    st.image("images/me.JPG")

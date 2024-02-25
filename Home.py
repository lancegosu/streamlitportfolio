import streamlit as st
import requests
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

st.set_page_config(page_title="Lance's Portfolio")
st.title("👋 Hello world! I'm Lance.")

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

image_path = "images/niagarafalls.jpg"
st.markdown(f'<div style="text-align: center;"><img src="{image_path}" alt="Image" /></div>', unsafe_allow_html=True)

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>

<h2>Automatic Slideshow</h2>
<p>Change image every 2 seconds:</p>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="/images/niagarafalls.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="images/niagarafalls.jpg" style="width:100%">
  <div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://unsplash.com/photos/zVhYcSjd7-Q/download?force=true&w=1920" style="width:100%">
  <div class="text">Caption Three</div>
</div>

</div>
<br>

<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>

<script>
let slideIndex = 0;
showSlides();

function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
</script>

</body>
</html> 

    """,
    height=600,
)

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

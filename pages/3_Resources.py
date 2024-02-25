import streamlit as st
from Home import add_logo

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("Educational content:")

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

st.markdown("[Harvard Online: CS50P - Introduction to Programming with Python](https://pll.harvard.edu/course/cs50s-introduction-programming-python)")
st.write("""
David Malan offers an accessible entry into the world of programming by teaching Python, 
a versatile and widely-used programming language known for its readability and flexibility. 
Python's prominence in artificial intelligence and machine learning applications adds an extra layer of significance to 
the course, making it an ideal starting point for those aspiring to go into the exciting realms of AI/ML.
""")

st.markdown("[fast.ai - Practical Deep Learning](https://course.fast.ai/)")
st.write("""
Created by Jeremy Howard and Rachel Thomas, the fast.ai course begins with offering a more hands-on approach 
by using AI tools in real-world examples before explaining how the tools work.
""")

st.markdown("[Andrej Karpathy's Neural Networks: Zero to Hero on YouTube](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)")
st.write("""
Andrej Karpathy's series of lectures describe the evolution of language modeling and how to build different 
architectural models from scratch to give a better understanding of the intricacies of modern language models.
""")

st.markdown("[DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)")
st.write("""
DeepLearning.AI covers various aspects of generative AI and is an excellent resource for both beginners and 
those looking to deepen their knowledge in the field.
""")

st.markdown("[Presentation: Fine-Tuning OpenAI’s GPT 3.5 to Unlock Enterprise Use Cases](https://exchange.scale.com/public/events/fine-tuning-open-ais-advanced-base-model-gpt-3-5-2023-11-08)")
st.write("""
Speakers Colin Jarvis and Luv Kothari emphasize the power of optimizing and fine-tuning LLMs for critical use cases to 
meet industry demands. They provide insights into the strategic balance (and difference) between 
retrieval augmented generation for content enrichment, and fine-tuning to enhance the model's capabilities. 
The presentation serves as a valuable guide for enterprises to ensure proficiency and confidence in harnessing 
transformative LLM capabilities.
""")

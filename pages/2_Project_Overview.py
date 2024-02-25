import streamlit as st
from Home import add_logo

st.set_page_config(page_title="Lance's Portfolio")
st.title("AI Projects")

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

st.write("""
My goal in creating AI projects is to harness the transformative capabilities of Large Language Models (LLMs) and 
seamlessly integrate them into diverse applications. By leveraging the power of LLMs, I aim to enhance the 
intelligence, functionality, and user experience of these applications, pushing the boundaries of what AI can achieve 
in various domains. This endeavor reflects my commitment to unlocking the full potential of artificial intelligence to 
drive innovation and elevate the impact of technology in our daily lives.
""")

l, c, r = st.columns(3)
with c:
    st.image("images/sf-ai.jpg")

st.write("""
[SpotOn](https://spoton.streamlit.app/) is a web application that integrates the OpenAI API with the Google Places 
API, resulting in a question-answering platform about place reviews.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
        - **Review-based Q&A**: Leverage place reviews to answer user queries using OpenAI's GPT-3.5-turbo language model.
        - **Place Search**: Utilize the Google Places API to search for places based on user queries.
        - **Interactive Map**: Display search results on an interactive map for enhanced user experience.

        **APIs**: OpenAI API, Google Places API, Google Maps API

        **Libraries**: requests
        """)

st.write("""
[Qdoc](https://qdocst.streamlit.app/) is a web application that utilizes a LLM to summarize articles and PDFs from a 
given URL. Additionally, it can answer questions related to the article using the conversation history, 
the article's content, and common knowledge.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Summarization from URL**: Summarize the contents of an article or PDF by providing a URL.
    - **Question-Answering**: Generates answers based on article content and conversation history.
    - **Conversation History**: Ask follow-up questions based on the ongoing conversation.

    **APIs**: OpenAI API

    **Libraries**: OpenAI, requests, BeautifulSoup, PyMuPDF
    """)

st.write("""
[CooPA](https://coopas.streamlit.app/) is a chatbot that uses the OpenAI API to deliver contextually informed answers 
by aggregating relevant content from Google search based on user queries.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Smart Search**: Aggregates content from relevant articles on Google search.
    - **Language Model Interaction**: Utilize OpenAI's GPT-3.5-turbo for generating contextually informed responses to user queries.
    - **Citation**: Automatically include source URLs when presenting the aggregated content, offering transparency and credibility.

    **APIs**: OpenAI API, Google Custom Search API

    **Libraries**: OpenAI, requests, BeautifulSoup
    """)

st.write("""
[aiXtensions](https://github.com/lancegosu/aixtensions) consists of two independent Chrome extensions: 
LookItUp and Persona, each leveraging OpenAI API for text-related tasks.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **LookItUp**: Allows users to define highlighted text on a webpage using OpenAI's GPT-3.5-turbo.
    - **Persona**: Transforms highlighted text into different styles of language using OpenAI's GPT-3.5-turbo.

    **APIs**: OpenAI API
    """)

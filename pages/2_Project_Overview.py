import streamlit as st

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("Personal AI Projects")

st.sidebar.header('Project Links')
st.sidebar.markdown('[SpotOn](https://spoton.streamlit.app/)')
st.sidebar.markdown('[Qdoc](https://qdocst.streamlit.app/)')
st.sidebar.markdown('[CooPA](https://coopas.streamlit.app/)')

st.sidebar.header('Contact Info')
st.sidebar.markdown("[Email](mailto:lancemnguyen@gmail.com)")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/lancedin)")
st.sidebar.markdown("[Github](https://github.com/lancegosu)")

st.write("My goal in creating AI projects is to harness the transformative capabilities of Large Language Models (LLMs) and seamlessly integrate them into diverse applications. By leveraging the power of LLMs, I aim to enhance the intelligence, functionality, and user experience of these applications, pushing the boundaries of what AI can achieve in various domains. This endeavor reflects my commitment to unlocking the full potential of artificial intelligence to drive innovation and elevate the impact of technology in our daily lives.")

st.write("[SpotOn](https://spoton.streamlit.app/) is a web application that integrates OpenAI's GPT-3.5-turbo language model with the Google Places API. This fusion results in a sophisticated platform for place search and intelligent question-answering.")
with st.expander("**Key Features**:"):
    st.markdown("""
        - **Review-based Q&A**: Leverage place reviews to answer user queries using OpenAI's GPT-3.5-turbo language model.
        - **Place Search**: Utilize the Google Places API to search for places based on user queries.
        - **Interactive Map**: Display search results on an interactive map for enhanced user experience.
        - **Dynamic UI**: Dynamically update the interface to allow users to ask questions about selected places and receive AI-generated responses.
        
        **APIs**: OpenAI ChatGPT API, Google Places API, Google Maps API
        
        **Libraries**: requests
        """)

st.write("[Qdoc](https://qdocst.streamlit.app/) is a web application that utilizes a Large Language Model (LLM) to summarize articles from a given URL or PDF. Additionally, it can answer questions related to the article using the conversation history, the article's content, and common knowledge.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Summarization from URL or PDF**: Summarize the contents of an article by providing a URL or PDF link.
    - **Question-Answering**: Inquire about specific details or seek clarification regarding the article, and the system generates answers based on conversation history and article content.
    - **Conversation History**: Ask follow-up questions based on the ongoing conversation.
    - **Refresh Conversation**: Clear the conversation history to initiate a fresh dialogue.
    
    **APIs**: OpenAI ChatGPT API
    
    **Libraries**: OpenAI, requests, BeautifulSoup, PyMuPDF
    """)

st.write("[CooPA](https://coopas.streamlit.app/) is a web application that leverages OpenAI's ChatGPT API and the Google Custom Search API to deliver contextually informed answers by aggregating relevant content from online articles based on user queries.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Smart Search**: Perform intelligent searches using Google Custom Search and aggregate content from relevant articles to generate comprehensive answers.
    - **Language Model Interaction**: Utilize OpenAI's GPT-3.5-turbo for generating contextually informed responses to user queries.
    - **Speech Recognition and Synthesis**: Enable users to input queries through speech and listen to the synthesized responses.
    - **Source Attribution**: Automatically include source URLs when presenting the aggregated content, offering transparency and credibility.
    
    **APIs**: OpenAI ChatGPT API, Google Custom Search API
    
    **Libraries**: OpenAI, requests, BeautifulSoup
    """)

st.write("[aiXtensions](https://github.com/lancegosu/aixtensions) consists of two independent Chrome extensions: LookItUp and Persona, each leveraging OpenAI's ChatGPT API for text-related tasks.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **LookItUp**: Allows users to define highlighted text on a webpage using OpenAI's GPT-3.5-turbo.
    - **Persona**: Transforms highlighted text into different styles of language using OpenAI's GPT-3.5-turbo.

    **APIs**: OpenAI ChatGPT API
    """)

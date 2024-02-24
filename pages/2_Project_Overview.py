import streamlit as st

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("AI Projects")

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

st.write("My goal in creating AI projects is to harness the transformative capabilities of Large Language Models (LLMs) and seamlessly integrate them into diverse applications. By leveraging the power of LLMs, I aim to enhance the intelligence, functionality, and user experience of these applications, pushing the boundaries of what AI can achieve in various domains. This endeavor reflects my commitment to unlocking the full potential of artificial intelligence to drive innovation and elevate the impact of technology in our daily lives.")

st.write("[SpotOn](https://spoton.streamlit.app/) is a web application that integrates the OpenAI API with the Google Places API, resulting in a question-answering platform about place reviews.")
with st.expander("**Key Features**:"):
    st.markdown("""
        - **Review-based Q&A**: Leverage place reviews to answer user queries using OpenAI's GPT-3.5-turbo language model.
        - **Place Search**: Utilize the Google Places API to search for places based on user queries.
        - **Interactive Map**: Display search results on an interactive map for enhanced user experience.
        
        **APIs**: OpenAI ChatGPT API, Google Places API, Google Maps API
        
        **Libraries**: requests
        """)

st.write("[Qdoc](https://qdocst.streamlit.app/) is a web application that utilizes a LLM to summarize articles and PDFs from a given URL. Additionally, it can answer questions related to the article using the conversation history, the article's content, and common knowledge.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Summarization from URL**: Summarize the contents of an article or PDF by providing a URL.
    - **Question-Answering**: Inquire about specific details or seek clarification regarding the article, and the system generates answers based on conversation history and article content.
    - **Conversation History**: Ask follow-up questions based on the ongoing conversation.
    
    **APIs**: OpenAI ChatGPT API
    
    **Libraries**: OpenAI, requests, BeautifulSoup, PyMuPDF
    """)

st.write("[CooPA](https://coopas.streamlit.app/) is a chatbot that uses the OpenAI API to deliver contextually informed answers by aggregating relevant content from Google search based on user queries.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Smart Search**: Aggregates content from relevant articles on Google search.
    - **Language Model Interaction**: Utilize OpenAI's GPT-3.5-turbo for generating contextually informed responses to user queries.
    - **Citation**: Automatically include source URLs when presenting the aggregated content, offering transparency and credibility.
    
    **APIs**: OpenAI ChatGPT API, Google Custom Search API
    
    **Libraries**: OpenAI, requests, BeautifulSoup
    """)

st.write("[aiXtensions](https://github.com/lancegosu/aixtensions) consists of two independent Chrome extensions: LookItUp and Persona, each leveraging OpenAI API for text-related tasks.")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **LookItUp**: Allows users to define highlighted text on a webpage using OpenAI's GPT-3.5-turbo.
    - **Persona**: Transforms highlighted text into different styles of language using OpenAI's GPT-3.5-turbo.

    **APIs**: OpenAI ChatGPT API
    """)

import streamlit as st
from Home import add_logo

st.set_page_config(page_title="Lance's Portfolio")
st.title("AI Projects")

add_logo()

st.sidebar.header('Project Links')
st.sidebar.caption('[LLM Optimization with RAG](https://lcrags.streamlit.app/)')
st.sidebar.caption('[SpotOn (Review Analysis)](https://spoton.streamlit.app/)')
st.sidebar.caption('[Qdoc (Article Assistant)](https://qdocst.streamlit.app/)')
st.sidebar.caption('[CooPA (Search Chatbot)](https://coopas.streamlit.app/)')

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
[LLM Optimization with RAG](https://lcrags.streamlit.app/) allows users to connect their data with an LLM and use it to generate a response.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
        - **Retrieval-Augmented Generation**: Connects user data with an LLM.
        - **LLM Optimization**: Optimizes advanced indexing, vector store embeddings, and retrieval mechanisms.
        - **File Upload**: Temporarily stores user uploaded files to interact with the RAG system.

        **APIs**: OpenAI API

        **Libraries**: LangChain
        """)

st.write("""
[SpotOn](https://spoton.streamlit.app/) is a review analysis application that integrates OpenAI API with Google Places 
API, resulting in a question-answering platform about place reviews.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
        - **Review-based Q&A**: Leverages place reviews to answer user queries using GPT-3.5-turbo.
        - **Place Search**: Utilizes the Google Places API to search for places.
        - **Interactive Map**: Displays search results on an interactive map for enhanced user experience.

        **APIs**: OpenAI API, Google Places API, Google Maps API

        **Libraries**: requests
        """)

st.write("""
[Qdoc](https://qdocst.streamlit.app/) is an article assistant that utilizes an LLM to summarize articles and PDFs from a 
given URL. Additionally, it can answer questions regarding the article using the history of the conversation, 
the article's content, and common knowledge.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Summarization from URL**: Summarizes the contents of an article or PDF by providing a URL.
    - **Question-Answering**: Generates answers based on article content and conversation history.
    - **Conversation History**: Ask follow-up questions based on the ongoing conversation.

    **APIs**: OpenAI API

    **Libraries**: OpenAI, requests, BeautifulSoup, PyMuPDF
    """)

st.write("""
[CooPA](https://coopas.streamlit.app/) is a chatbot that uses OpenAI API to deliver contextually informed answers 
by aggregating relevant content from Google search based on user queries.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **Smart Search**: Aggregates content from relevant articles on Google search based on user queries.
    - **Language Model Interaction**: Utilizes GPT-3.5-turbo for generating contextually informed responses.
    - **Citation**: Automatically includes source URLs of the articles, offering transparency and credibility.

    **APIs**: OpenAI API, Google Custom Search API

    **Libraries**: OpenAI, requests, BeautifulSoup
    """)

st.write("""
[AI Extensions](https://github.com/lancegosu/AI-Extensions) currently consists of two independent Chrome extensions: 
LookItUp and Persona, each leveraging OpenAI's GPT-3.5-turbo for text-related tasks.
""")
with st.expander("**Key Features**:"):
    st.markdown("""
    - **LookItUp**: Allows users to define highlighted text on a webpage.
    - **Persona**: Transforms highlighted text into different styles of language.

    **APIs**: OpenAI API
    """)

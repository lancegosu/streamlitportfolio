import streamlit as st

st.set_page_config(page_title="Lance's Portfolio", layout='wide')
st.title("Educational content:")

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

st.markdown("[Harvard Online: CS50P - Introduction to Programming with Python](https://pll.harvard.edu/course/cs50s-introduction-programming-python)")
st.write("David Malan teaches an enriching course that offers a comprehensive and accessible entry into the world of programming. This course introduces Python, a versatile and widely-used programming language known for its readability and flexibility. Python's prominence in artificial intelligence and machine learning applications adds an extra layer of significance to the course, making it an ideal starting point for those aspiring to go into the exciting realms of AI/ML.")

st.markdown("[fast.ai - Practical Deep Learning](https://course.fast.ai/)")
st.write("The fast.ai course is a cutting-edge, practical deep learning program that stands out for its accessibility and effectiveness in teaching complex concepts. Created by renowned AI researchers Jeremy Howard and Rachel Thomas, the course prioritizes a hands-on approach, enabling students to quickly grasp and implement state-of-the-art deep learning techniques. With a focus on real-world applications and a commitment to democratizing AI education, fast.ai empowers learners to rapidly advance their skills and contribute to the transformative field of artificial intelligence.")

st.markdown("[Andrej Karpathy's Neural Networks: Zero to Hero on YouTube](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)")
st.write("Andrej Karpathy's series of lectures provides an insightful journey through the evolution of language modeling. Across eight videos, he delves into the fundamentals of neural networks and backpropagation, constructing a language model (makemore) with emphasis on components like MLP, activations, gradients, and BatchNorm. The series culminates in the creation of a WaveNet and a comprehensive walkthrough on building GPT (Generative Pre-trained Transformer) from scratch. Karpathy's engaging presentations demystify the complexities, making it an invaluable resource for understanding the intricacies of modern language models.")

st.markdown("[DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)")
st.write("DeepLearning.AI's short courses cover various aspects of generative AI. Learn from industry experts like Andrew Ng and develop practical skills in areas such as chatbot building, finetuning large language models, and evaluating model safety. With a focus on practical applications and real-world examples, these courses cater to learners seeking a foundational understanding of deep learning techniques, making them an excellent resource for both beginners and those looking to deepen their knowledge in the field.")

st.markdown("[Presentation: Fine-Tuning OpenAI’s GPT 3.5 to Unlock Enterprise Use Cases](https://exchange.scale.com/public/events/fine-tuning-open-ais-advanced-base-model-gpt-3-5-2023-11-08)")
st.write("Colin Jarvis from OpenAI and Luv Kothari from Scale unveil the power of fine-tuning large language models (LLMs) for enterprise use cases. This presentation explores optimizing fine-tuning for critical use cases, emphasizing tailored LLMs to meet industry demands. Focusing on retrieval augmented generation (RAG), which can seamlessly integrate with fine-tuning, they provide insights into the strategic balance between RAG for content enrichment and fine-tuning to enhance the model's capabilities. Providing a dynamic solution for unlocking OpenAI's GPT-3.5 potential, this session is a valuable guide for enterprises in the evolving landscape of language models and ensures proficiency and confidence in harnessing transformative LLM capabilities.")

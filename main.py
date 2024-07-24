import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("imagefiles/12.png", width=450)

with col2:
    st.title("Wajeeha Aftab")
    content = """ Hi, I am Wajeeha Aftab! I am a software engineer. I have a passion for learning and sharing my knowledge with others as much as I can. 
    I have a strong background in Python, SQL, and Machine Learning. I am always eager to learn new technologies and tools. I am a quick learner and a team player.
      I am always ready to take on new challenges and work on exciting projects. I am looking for opportunities to grow and develop my skills further. """
    st.info(content) 
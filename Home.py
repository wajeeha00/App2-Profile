import pandas as pd
import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("imagefiles/w.jfif", width=400)

with col2:
    st.title("Wajeeha Aftab")
    content = """ Hi, I am Wajeeha Aftab! I am a software engineer. I have a passion for learning and sharing my knowledge with others as much as I can. 
    I have a strong background in Python, SQL, and Machine Learning. I am always eager to learn new technologies and tools. I am a quick learner and a team player.
      I am always ready to take on new challenges and work on exciting projects. I am looking for opportunities to grow and develop my skills further. """
    st.info(content) 

st.write("## Projects")
st.write("Below are some of the projects I have worked on.Feel free to check them out!")
#title;description;url;image
df = pd.read_csv('data.csv',sep=';')


col3,empty_col, col4= st.columns([1.5,0.5,1.5])
with col3:
    for index,row in df[:10].iterrows():
        st.write(f"### {row['title']}")
        st.image("imagefiles/"+row["image"], width=200)
        st.write(row['description'])
        st.write(f"Project URL: {row['url']}")

with col4:
    for index,row in df[10:].iterrows():
        st.write(f"### {row['title']}")
        st.image(f"imagefiles/{index+1}.png", width=200)
        st.write(row['description'])
        st.write(f"Project URL: {row['url']}")
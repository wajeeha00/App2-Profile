import streamlit as st
from send_email import send_email
st.header("Contact Us")
with st.form(key ="email_form"):
    user_email = st.text_input("Enter your email")
    message = st.text_area("Enter your message")
    submit = st.form_submit_button("Submit")
    message = f"""\
    Subject: New Email from {user_email}
    from {user_email}
    {message}
"""
    if submit:
        send_email(message)
        st.info("Email sent successfully!")
import streamlit as st

st.title("Message Processor")

message = st.text_input("Enter your message")

if st.button("Process Message"):
    st.write("You entered:")
    st.write(message)

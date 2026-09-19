import streamlit as st
import requests

st.title("Message Processor")

message = st.text_input("Enter your message")

if st.button("Process Message"):

    response = requests.post(
        "http://localhost:8000/process",
        params={"message": message}
    )

    result = response.json()

    st.subheader("Result")
    st.write(result["message"])
    st.write(f"Characters: {result['length']}")

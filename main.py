import os
from langchain_ollama import ChatOllama
import streamlit as st

st.set_page_config(page_title="💬 | Chat",layout="centered")
st.title("🤖 Generative AI Chatbot")


if "chat_history" not in st.session_state:
    st.session_state.chat_history=[]

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])



llm=ChatOllama(model="qwen2.5-3b-local:latest", temperature=0.0,)

user_prompt=st.chat_input("Ask chatbot")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    response =llm.invoke(input=[{"role":"system","content":"You are a helpful assistant. Please give me precise answers"},*st.session_state.chat_history])

    assistant_response=response.content

    st.session_state.chat_history.append({"role":"assistant","content":assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)






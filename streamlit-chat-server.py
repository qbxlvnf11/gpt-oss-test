import streamlit as st
import requests
import json

## 페이지 설정
st.set_page_config(page_title="GPT-OSS Chat", page_icon="🤖", layout="centered")
st.title("GPT-OSS Chat Room")

## 대화 히스토리
if "messages" not in st.session_state:
    st.session_state["messages"] = []

## 이전 메시지 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

## 사용자 입력
if prompt := st.chat_input("메시지를 입력하세요..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    print(' ===> st.session_state.messages[-3:]:', st.session_state.messages[-3:])
    
    with st.chat_message("user"):
        st.markdown(prompt)

    ## Ollama API 요청
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gpt-oss:20b",
            "messages": st.session_state.messages,
            "stream": False
        }
    )

    if response.status_code == 200:
        content = response.json()["message"]["content"]
        
        print(' ===> Response:', content)
        
        st.session_state.messages.append({"role": "assistant", "content": content})
        with st.chat_message("assistant"):
            st.markdown(content)
    else:
        st.error(f"Error: {response.text}")


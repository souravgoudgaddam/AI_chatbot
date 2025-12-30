import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat/"

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call FastAPI backend
    response = requests.post(
        API_URL,
        json={"message": user_input}
    )

    if response.status_code == 200:
        bot_reply = response.json()["reply"]
    else:
        bot_reply = "❌ Error connecting to backend."

    # Show bot message
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

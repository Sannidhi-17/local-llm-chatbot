import streamlit as st
from ollama import Client

client = Client()
st.title("💬 Gemma 3 4B Chatbot (Local)")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a friendly assistant."}]

# Clear chat button at top
if st.button("Clear Chat"):
    st.session_state.messages = []

# Chat input box
user_input = st.text_input("You:", "")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat(
        model="gemma3:4b",
        messages=st.session_state.messages
    )

    st.session_state.messages.append({
        "role": "assistant",
        "content": response.message.content
    })

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div style='text-align:right; background-color:#1f77b4; color:white; padding:10px; border-radius:10px; margin:5px 0; max-width:80%; float:right; clear:both;'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    elif msg["role"] == "assistant":
        st.markdown(
            f"<div style='text-align:left; background-color:#333333; color:white; padding:10px; border-radius:10px; margin:5px 0; max-width:80%; float:left; clear:both;'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

# app.py

import os
import streamlit as st
from openai import AzureOpenAI

# Environment variables
endpoint = os.getenv("ENDPOINT_URL", "https://fadi-user28--resource.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4.1-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "3uz4y04LltIk1khjGwqnScRWR033A4saeE8GCKOKv9F16INO8ID0JQQJ99BGACYeBjFXJ3w3AAAAACOGCTo5")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Streamlit UI
st.set_page_config(page_title="Intel Support Bot", page_icon="🤖")
st.title("🤖 Intel Support Bot")

# User input
user_input = st.text_area("Ask a question:", "", height=100)

if st.button("Get Answer") and user_input.strip():
    # Build chat messages
    messages = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are IntelSupportBot, a helpful assistant for Intel employees."
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_input
                }
            ]
        }
    ]

    # Get completion
    with st.spinner("Getting answer..."):
        response = client.chat.completions.create(
            model=deployment,
            messages=messages,
            max_tokens=500,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )

    answer = response.choices[0].message.content
    st.success("✅ Answer:")
    st.write(answer)

import streamlit as st
import requests
import os

# Title of the App
st.title("🤖 Gen AI DEVOPS SHOP")
st.subheader("Powered by Gemini 2.5 Pro & GKE")

# Get Backend URL from Environment Variable (or use localhost for testing)
# IN KUBERNETES, we will set this to the Backend Service Name
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8080")

# Input box
user_input = st.text_input("Ask me about products or DevOps:", "")

if st.button("Generate Answer"):
    if user_input:
        with st.spinner("Asking Gemini..."):
            try:
                # Send request to the Backend API
                payload = {"prompt": user_input}
                response = requests.post(f"{BACKEND_URL}/generate", json=payload)
                
                if response.status_code == 200:
                    answer = response.json().get("response", "No response found.")
                    st.success(answer)
                else:
                    st.error(f"Error: {response.text}")
            except Exception as e:
                st.error(f"Connection failed: {e}")
    else:
        st.warning("Please enter a prompt.")

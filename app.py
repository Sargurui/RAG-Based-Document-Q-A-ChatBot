import os
import streamlit as st
from load_documents import load_documents, add_documents_to_index, retrieve_relevant_documents
from gemini import generate_response
from utils import load_env

# Load environment variables
load_env()

# Set page configuration for dark theme
st.set_page_config(
    page_title="RAG Based with Document Upload",
    page_icon=":robot_face:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for dark theme
st.markdown(
    """
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    .sidebar .sidebar-content {
        background-color: #2e2e2e;
    }
    .css-1d391kg p {
        color: #ffffff;
    }
    .css-1cpxqw2 a {
        color: #1e90ff;
    }
    .css-1cpxqw2 p {
        color: #ffffff;
    }
    .stTextInput input {
        background-color: #3e3e3e;
        color: #ffffff;
    }
    .stButton button {
        background-color: #4e4e4e;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
def main():
    st.title("RAG Based  Document Q&A ChatBot")

    # Sidebar for file uploads
    st.sidebar.header("Upload Documents")
    uploaded_files = st.sidebar.file_uploader(
        "Upload .txt, .pdf, .docx, or .xlsx files", 
        type=["txt", "pdf", "docx", "xlsx"], 
        accept_multiple_files=True
    )
    
    global documents

    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = f"temp/{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.read())
            load_documents(file_path)
        add_documents_to_index()
        st.sidebar.success(f"{len(uploaded_files)} file(s) processed and added to the index!")

    # Initialize chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Chat interface
    st.header("Chat")
    user_query = st.text_input("Enter your query:", key="user_query")
    if st.button("Send"):
        if user_query.strip():
            retrieved_docs = retrieve_relevant_documents(user_query)
            
            # Add user query to chat history
            st.session_state.history.append({"user": user_query})
            
            # Generate response based on chat history and retrieved documents
            bot_response = generate_response(user_query, retrieved_docs, st.session_state.history)

            # Add bot response to chat history
            st.session_state.history.append({"bot": bot_response})

            # Display only the current bot response (not the whole history)
            st.markdown(f"**Chatbot**: {bot_response}")

if __name__ == "__main__":
    # Ensure the temp directory exists
    if not os.path.exists("temp"):
        os.makedirs("temp")
    
    # Run Streamlit app
    main()

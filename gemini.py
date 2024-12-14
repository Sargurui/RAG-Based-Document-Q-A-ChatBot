import google.generativeai as genai
from utils import load_env
import os

# Load environment variables
load_env()
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Configure Google Gemini API
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create Gemini model and start chat session
gemini_model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",  # Specify the Gemini model
    generation_config=generation_config,
)

chat_session = gemini_model.start_chat(
    history=[]
)

# Function to generate a response using Google Gemini API
def generate_response(query, retrieved_docs, chat_history):
    # Combine query and retrieved documents as context
    context = "\n".join(retrieved_docs)
    prompt = f"""
    You are an intelligent assistant. Use the context below to answer the query:
    
    Context:
    {context}
    
    History:
    {chat_history}
    
    Query:
    {query}
    """
    # Generate response using the chat session
    try:
        response = chat_session.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        st.error(f"Error generating response: {e}")
        return "Sorry, I couldn't generate a response."

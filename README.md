# 📄 **RAG-Based Document Upload Chatbot**

This project is a **Retrieval-Augmented Generation (RAG)**-based chatbot built with **Streamlit**. It allows users to upload documents, ask queries, and receive context-aware responses from the document data.

---

## 🚀 **Features**

- **Document Upload**: Supports `.txt`, `.pdf`, `.docx`, and `.xlsx` file uploads.
- **Intelligent Responses**: Answers queries using **retrieved document content** and a conversational context.
- **Interactive UI**: A clean and user-friendly interface with a modern dark theme.
- **Chat History**: Maintains query and response history for a seamless conversation.

---

## 🛠️ **Technologies Used**

- **Python**: Backend logic for processing and retrieving document content.
- **Streamlit**: Framework for the web interface.
- **Custom Libraries**:  
   - `load_documents.py`: Loads and processes uploaded documents.  
   - `gemini.py`: Handles the generation of responses using the RAG approach.  
   - `utils.py`: Manages helper functions like environment setup.  

---

## 📂 **Project Structure**

```
📁 RAG-Based-Document-Chatbot/
│
├── app.py                 # Main Streamlit app
├── load_documents.py      # Document upload and processing logic
├── gemini.py              # Response generation logic
├── utils.py               # Utility functions and environment loader
├── temp/                  # Temporary storage for uploaded files
├── requirements.txt       # Project dependencies
└── README.md              # Documentation (this file)
```

---

## 💻 **Installation and Setup**

Follow these steps to run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/rag-document-chatbot
cd rag-document-chatbot
```

### 2. Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

### 4. Access the Application
Open your browser and navigate to:  
**`http://localhost:8501`**

---

## 🎯 **Usage**

1. **Upload Documents**:  
   - Use the sidebar to upload `.txt`, `.pdf`, `.docx`, or `.xlsx` files.  
   - Uploaded documents will be processed and indexed automatically.

2. **Ask Queries**:  
   - Enter your question or query in the chatbox.  
   - The chatbot will retrieve relevant information from the documents and generate a response.

3. **View Responses**:  
   - Responses are generated in real-time and displayed under the chat interface.  

---

## 🥩 **Future Enhancements**

- Integrate advanced language models for better responses.  
- Support for more file formats.  
- Add a downloadable chat transcript feature.  
- Multi-user authentication for secure access.  

---

## 🤝 **Contributions**

Contributions are welcome! Follow these steps:  
1. **Fork** the repository.  
2. **Create a new branch**:  
   ```bash
   git checkout -b feature-branch
   ```
3. **Make your changes** and commit:  
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push** to your branch:  
   ```bash
   git push origin feature-branch
   ```
5. Submit a **Pull Request**.




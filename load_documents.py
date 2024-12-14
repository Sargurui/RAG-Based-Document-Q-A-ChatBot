import os
import pdfplumber
import docx
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# List to store documents
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize FAISS Index
dimension = 384  # Embedding size for all-MiniLM-L6-v2
index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity search
documents = []  # Store the original documents

# Function to load text from .txt files
def load_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# Function to load text from .pdf files
def load_pdf(file_path):
    pdf_text = []
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pdf_text.extend([line.strip() for line in text.split('\n') if line.strip()])
    return pdf_text

# Function to load text from .docx files
def load_docx(file_path):
    doc = docx.Document(file_path)
    return [para.text.strip() for para in doc.paragraphs if para.text.strip()]

# Function to load text from .xlsx files
def load_xlsx(file_path):
    excel_text = []
    df = pd.read_excel(file_path)  # Read the Excel file into a DataFrame
    for column in df.columns:
        # Iterate over each cell in the column
        excel_text.extend([str(cell).strip() for cell in df[column] if pd.notnull(cell)])
    return excel_text

# General function to load documents from different file types
def load_documents(file_path):
    global documents
    file_extension = os.path.splitext(file_path)[-1].lower()
    if file_extension == ".txt":
        documents.extend(load_txt(file_path))
    elif file_extension == ".pdf":
        documents.extend(load_pdf(file_path))
    elif file_extension == ".docx":
        documents.extend(load_docx(file_path))
    elif file_extension == ".xlsx":
        documents.extend(load_xlsx(file_path))
    else:
        st.warning(f"Unsupported file type: {file_extension}")

# Function to add documents to the FAISS index
def add_documents_to_index():
    global documents
    embeddings = model.encode(documents)
    index.add(np.array(embeddings, dtype=np.float32))

# Function to retrieve relevant documents based on the query
def retrieve_relevant_documents(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding, dtype=np.float32), top_k)
    retrieved_docs = [documents[idx] for idx in indices[0]]
    return retrieved_docs
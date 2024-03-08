import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai


load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text



def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=10000)
    chunks=text_splitter.split_text(text)
    
    
def get_vector_store(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="model/embedding-001")
    vector_store=FAISS.from_text(text_chunks,embedding=embeddings)
    vector_store.save_local("faiss-index")
    
    
def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    
    model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3)
    
    PromptTemplate(template=prompt_template,input_variables=["context","question"])
    chain=load_qa-chain(model,chain_type="stuff",prompt=prompt)
    return chain
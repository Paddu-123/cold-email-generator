from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from bs4 import BeautifulSoup
import requests
from chromadb import Client
from chromadb.config import Settings

groq_api = "YOUR_API_KEY"

def extract_jobs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.get_text()
    return jobs

def generate_email(job_info):
    llm = ChatGroq(model="llama-3.1-70b-versatile", api_key=groq_api)
    message = HumanMessage(content=f"Generate a cold email for this job:\n\n{job_info}")
    response = llm.invoke([message])
    return response.content

def full_pipeline(url):
    job_text = extract_jobs(url)
    email = generate_email(job_text)
    return email

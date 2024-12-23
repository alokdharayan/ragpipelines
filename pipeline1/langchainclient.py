import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama

load_dotenv()

OLLAMA_SERVER_URL = os.environ['OLLAMA_SERVER_URL']
print(OLLAMA_SERVER_URL)

llm = Ollama(model="llama3.2", base_url=OLLAMA_SERVER_URL)

response = llm.invoke("hi, how are you?")
print(response)
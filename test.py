from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    api_key = API_KEY
)

response = llm.invoke("What is the capital of France?")
print(response.content)
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    api_key = API_KEY
)

system_instruction = """
- You are an Ai travel assistant,
- answer only travel related questions,
- if the question is not related to travel, answer "sorry I am a travel assistant, I can only answer travel related
"""

prompt = ChatPromptTemplate([
    ('system', system_instruction),
    ('user', '{input}')
])
chain = prompt | llm
question = input('You:')
response = chain.invoke({"input": question})
print(response.content)

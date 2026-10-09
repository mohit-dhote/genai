from langchain_groq import ChatGroq

API_KEY = "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"

llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    api_key = API_KEY
    
)
response = llm.invoke("What is the capital of France?")
print(response.content)
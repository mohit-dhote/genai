from langchain_groq import ChatGroq
# if wanted to write output in the specific format use this 
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv('API_KEY')

# LLM objects 
llm = ChatGroq(
    model = 'openai/gpt-oss-120b',
    api_key = api_key
)

invoice_text = """
Date: 10/01/2026  
Patient Name: Sibesh Patel  
Patient ID: P-10245  
Doctor: Dr. Alok Mehta  
Department: Cardiology  
Bill #: HB-2026-001  

Services Rendered:  
Consultation Fee - 300  
X-Ray Imaging - 250  
Blood Test - 150  
Medication Charges - 200  
Room Charges (2 days) - 1000  
Service Tax (5%) - 95  

Payment Method: Credit Card  
Total Amount: 1995  
"""

# define JSON output parser
output_parser = JsonOutputParser()
format_instructions = output_parser.get_format_instructions()

prompt = ChatPromptTemplate.from_template(
    """
    Refer to the hospital bill below and return it in JSON format.
    {invoice}
    {instructions}
    """
)

chain = prompt | llm | output_parser

response = chain.invoke({
    "invoice": invoice_text,
    "instructions": format_instructions
})

print(response)
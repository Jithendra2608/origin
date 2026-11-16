import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

ACTIVE_MODELS = [
    "gemini-3.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-3.7-flash",
    "gemini-3.8-flash"
]

def get_structured_chain(prompt, schema_class):
    """
    Creates a LangChain pipeline with automatic fallback across active models.
    """
    chains = []
    for model_name in ACTIVE_MODELS:
        llm = ChatGoogleGenerativeAI(
            model=model_name,
            max_retries=0,
            timeout=20
        ).with_structured_output(schema_class)
        chains.append(prompt | llm)
    
    return chains[0].with_fallbacks(chains[1:])

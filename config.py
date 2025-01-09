import os
from dotenv import load_dotenv

class Config:    
    """Configuration class for the application."""
    load_dotenv()
    FLASK_DEBUG = os.getenv("FLASK_DEBUG")
    OPENAI_KEY = os.getenv('OPENAI_KEY')  # OpenAI API key
    TEMPLATES_AUTO_RELOAD = os.getenv('TEMPLATES_AUTO_RELOAD')  
    ASSISTANT_ID = os.getenv('ASSISTANT_ID')  # OpenAI Assistant ID
    
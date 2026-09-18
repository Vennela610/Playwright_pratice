import os 
from dotenv import load_dotenv 

load_dotenv()
class Config:
    parabank_API_base_url = os.getenv("parabank_API_base_url")
    parabank_API_username = os.getenv("parabank_API_username")
    parabank_API_password = os.getenv("parabank_API_password")
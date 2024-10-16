import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_TOKEN=os.getenv('OPENAI_TOKEN')
TELEGRAM_TOKEN=os.getenv('TELEGRAM_TOKEN')
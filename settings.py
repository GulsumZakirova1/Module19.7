import os

from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv("valid_email")
valid_password = os.getenv("valid_password")

mistaken_email = os.getenv("mistaken_email")
invalid_password = os.getenv("invalid_password")


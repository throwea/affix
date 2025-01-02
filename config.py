import os

from dotenv import load_dotenv

load_dotenv(override=True)  # override option ensure System Env variables are overriden

#WARN: if I'm seeing conflicts with other environment variables during local development just use a json config file
# All .env variables
BDOOR = os.environ["BDOOR"]
OPENAI_KEY = os.environ["OPENAI_KEY"]
AFFIX_DB_URL = os.environ["AFFIX_DB_URL"]

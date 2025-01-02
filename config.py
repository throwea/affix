import os

from dotenv import load_dotenv

load_dotenv(override=True)  # override option ensure System Env variables are overriden

#WARN: if I'm seeing conflicts with other environment variables during local development just use a json config file
# All .env variables
DEV_KEY = os.environ["DEV_KEY"]
OPENAI_KEY = os.environ["OPENAI_KEY"]
AFFIX_DB_URL = os.environ["AFFIX_DB_URL"]

### This file will contain all the methods for connecting the third party LLM's
from openai import OpenAI
from config import OPENAI_KEY

client = OpenAI(
    api_key=OPENAI_KEY,  # This is the default and can be omitted
)

def query_openai(messages): #TODO: add typing for the messages
    '''
    This method is used for sending a request to OpenAI GPT models
    '''
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-4o",
    )
    return chat_completion

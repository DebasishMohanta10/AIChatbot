import openai
from django.conf import settings

openai.api_key =settings.API_KEY

def get_completion_from_message(messages,model='gpt-3.5-turbo',temperature=0):
    response = openai.ChatCompletion.create(
        messages=messages,
        model = model,
        temperature=temperature
    )
    return response.choices[0].message['content'] 
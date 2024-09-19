"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from tkinter import *

genai.configure(api_key="AIzaSyDorxcGq9iIcj4BzBY8c8B0y88K2I94oXA")


# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

history=[]

while True:
    chat_session = model.start_chat(
        history=history
    )
    user = input("You :")
    
    
    response = chat_session.send_message(user)

    answer=response.text
    print()
    print(f'AI :{answer}')
    
    
    history.append({"role": "user",
                    "parts": [user]})
    history.append({"role": "model",
                    "parts": [answer]})
    

from openai import OpenAI
import gradio as gr
from google.colab import userdata

client = OpenAI(
  api_key=userdata.get('anomix'),
  base_url="https://openrouter.ai/api/v1",
)

def chatbot_interface(message,history):
  try:
    user_input=[
      {
          "role":"user",
          "content":message
      }
  ]
    completion=client.chat.completions.create(
       model="deepseek/deepseek-chat-v3.1",
        messages=user_input
    )
    reply=completion.choices[0].message.content
    return reply

  except Exception as e:
    return e

iface=gr.ChatInterface(
    fn=chatbot_interface,
    title="ANOMIX HEALTH CHAT BOT",
    description="Welcome To Anomix Health Care Chat Bot What would You Like To Know" # Added the custom message here
)
iface.launch(share="TRUE")
from tensorflow.keras.models import load_model
import tensorflow_hub as hub 
import nv_utils as nvu
import openai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
openai.api_key = API_KEY

def check_text(text):
    text = nvu.clean_text(text)
    detector = load_model("fnd.h5",
                          custom_objects={'KerasLayer':hub.KerasLayer})
    return detector.predict([text])[0, 0]

def get_answer(context):
    prompt = context + "Summarise the above text in 20 words"
    return openai.ChatCompletion.create(
        messages=[{
            "role": "assistant",
            "content": prompt
        }],
        temperature=0,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        model="gpt-3.5-turbo"
        )["choices"][0]["message"]["content"]

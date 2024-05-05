from dotenv import load_dotenv
from groq import Groq
import json
import os
load_dotenv()

def ask_groq(parsed_bill):
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    # convert dictionary into json string
    json_string = json.dumps(parsed_bill)

    
    message = {
        "role": "user",
        "content": "Please summarize the legislation, highlighting its purpose and intent, key provisions, impacts and implications. Here is the bill in json format: " + json_string
    }

    # Get the Groq API to generate the text summary
    chat_completion = client.chat.completions.create(
        messages=[message],
        model="mixtral-8x7b-32768",
    )

    return chat_completion.choices[0].message.content
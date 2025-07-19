# all the online code is here !! 

import os
from openai import OpenAI

from dotenv import load_dotenv 
# import the load_dotenv so my .env file will be readable brother !! 

# making the open ai client !!!  means making the object of the openai class 

load_dotenv("/home/N3xthar-Voryx/AI-DEVOPS-COPILOT/.env") 
# specify the path if not in current folder !! 

client = OpenAI(api_key =os.getenv("OPEN_API_KEY")) 
# making the object of the openai that is client !! 


#   01              function for the explanation of linux command !! 

def explain_command_online(command__) :
    prompt = f"Explain me the linux commands in the easy way with the real world example \n{command__}"

    # api call 
    response  = client.chat.completions.create (
        # selecting the model !! 
        model = "gpt-4o",

        # need the input in the json format !!! 
        messages =[
            {
                "role":"user",                                              # need to define the who is speaking if not than the api will through the error !!! 
                "content":prompt
            }
        ]
    )
    return response.choices[0].message.content 

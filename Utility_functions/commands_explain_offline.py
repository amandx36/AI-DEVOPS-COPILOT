# all the offline code is here 

from ollama import Client

# making the client for ollama that is local LLM brother !!!

client = Client(host='http://localhost:11434')      # here is the ollama running locally !!! connect to it
model_name = 'codellama:7b'

#   01              function for the explanation of linux command !! 

def explain_command_offline(command__) :
    prompt = f"Explain me the linux commands in the easy way with the real world example \n{command__}"

    # api call 
    response = client.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response['message']['content']

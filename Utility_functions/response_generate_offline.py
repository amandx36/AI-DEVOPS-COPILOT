# all the offline code is here 

from ollama import Client

# making the client for ollama that is local LLM brother !!!

client = Client(host='http://localhost:11434')      # here is the ollama running locally !!! connect to it
model_name = 'codellama:7b'

#   01              function for the generation of linux command !! 

def response_generator_offline(task) :
    prompt = f"Generate the useful linux command or script to perform the following task \n{task}"

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

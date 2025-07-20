

# # use ollama for the local run and also open ai for the online brother 


import system_info
import typer       #  for the cli integration !! 
from commands_explain_online import explain_command_online     # if online mode than import the explain online command module
from commands_explain_offline import explain_command_offline            # else load  explain the offline mode command
from response_generate_offline import response_generator_offline       # for generating the response offline !!! 
from response_generator_online import response_generator_online        # for generating the response online !!!!! 
from system_info import get_system_information           # importing the function for getting the system information 






app = typer.Typer()      # module to read the text from the terminal after the python main.py "ls -a "


@app.command()
def main(
    mode: int = typer.Option(..., prompt="select the modoe 1 for online , 0 for offline "),
    task: str = typer.Option(..., prompt="what you have to perform example [explain ,generate ,system_info   !!!    ]"),
):
    if mode == 1:
        print("Enter into the online mode ")
        explain_command = explain_command_online    
    else:
        print("Entered into the offline mode ")
        explain_command  =  explain_command_offline    

    if task == "explain":
        cmd = typer.prompt("command to explain?")
        out = explain_command(cmd)              # to take the input from the user 
        print(out)

    elif task == "generate" :
        if mode == 1 :
            generate_command = response_generator_online
        else :
            generate_command = response_generator_offline

        response_input = typer.prompt("Describe the response you want to generate command/script ")

        output = generate_command(response_input)
        print(output)

    elif task =="system_info" :                     # for getting the system information   !!! 
        show = get_system_information()
        print(show)

    
   
    
    else:
        print("task not found.. Available task [explain , generate , system_info]")



if __name__ == "__main__":
    app()

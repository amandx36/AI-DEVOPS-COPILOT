

# # use ollama for the local run and also open ai for the online brother 


import system_info
import typer       #  for the cli integration !! 
from commands_online import explain_command_online     # if online mode than import the explain online command module
from commands_offline import explain_command_offline            # else load  explain the offline mode command

from system_info import get_system_information 

app = typer.Typer()      # module to read the text from the terminal after the python main.py "ls -a "


@app.command()
def main(
    mode: int = typer.Option(..., prompt="select the modoe 1 for online and 0 for offline "),
    task: str = typer.Option(..., prompt="what you have to perform example [explain , systeminfo!!!    ]"),
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

    elif task =="system_info" :                     # for getting the system information   !!! 
        show = get_system_information()
        print(show)

    
   
    
    else:
        print("task not found.. only 'explain' works rn")



if __name__ == "__main__":
    app()

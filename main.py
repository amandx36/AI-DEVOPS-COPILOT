

# # use ollama for the local run and also open ai for the online brother 


import typer       #  for the cli integration !! 

app = typer.Typer()      # module to read the text from the terminal after the python main.py "ls -a "


@app.command()
def main(
    mode: int = typer.Option(..., prompt="select the modoe 1 for online and 0 for offline "),
    task: str = typer.Option(..., prompt="what you have to perform example [explain ,  adding !!!    ]"),
):
    if mode == 1:
        print("Enter into the online mode ")
        from commands_online import explain_command_online as explain_command    # if online mode than import the explain online command module 
    else:
        print("Entered into the offline mode ")
        from commands_offline import explain_command_offline as explain_command     # else load  explain the offline mode command 

    if task == "explain":
        cmd = typer.prompt("command to explain?")
        out = explain_command(cmd)              # to take the input from the user 
        print(out)
    else:
        print("task not found.. only 'explain' works rn")

if __name__ == "__main__":
    app()

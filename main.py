import sys                # module to read the text from the terminal after the python main.py "ls -a "

mode = int(input("Enter 1 for the online mode else 0 for the offline mode "))
# use ollama for the local run and also open ai for the online brother 

if mode == 0 :
    from commands_offline import explain_command_offline as explain_command

else:
    from commands_online import explain_command_online as explain_command


# cli based input and the output broo !!! 

checker = input("Enter command type (e.g. explain): ")

if checker == "explain":
    cmd = input("Enter the command to explain: ")
    output = explain_command(cmd)
    print(output)
else:
    print("Unknown command !! ")

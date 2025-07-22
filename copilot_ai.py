

# # use ollama for the local run and also open ai for the online brother 


from re import S
from Utility_functions.git_helper import git_status
import typer       #  for the cli integration !! 


# our files inside the another files now we have to import with the folder_name.

from Utility_functions.commands_explain_online import explain_command_online     # if online mode than import the explain online command module
from Utility_functions.commands_explain_offline import explain_command_offline            # else load  explain the offline mode command
from Utility_functions.response_generate_offline import response_generator_offline       # for generating the response offline !!! 
from Utility_functions.response_generator_online import response_generator_online        # for generating the response online !!!!! 
from system_info import get_system_information           # importing the function for getting the system information 
from Utility_functions.daily_tips import  get_daily_tips            # importing for getting the daily tips brother !!! 
from Utility_functions.docker_helper import docker_run, show_containers , show_docker_images , docker_stop   # importing the docker container functions 
from Utility_functions.docker_helper import show_docker_images   # importing the docker images 
from Utility_functions.git_helper import git_add ,git_status , git_commit   #importing the git_helper file's functions !!! 
from Utility_functions.banner import show_banner



app = typer.Typer()

@app.command()
def main(
    mode: int = typer.Option(
        ...,
        prompt=(
            "\n"
            "╔══════════════════════════════════════════════════════════════╗\n"
            "║                   🌀  Welcome, Commander! 🌀                ║\n"
            "╠══════════════════════════════════════════════════════════════╣\n"
            "║ How do you want to work today?                              ║\n"
            "║                                                            ║\n"
            "║  1️⃣  Online  (AI Magic - Internet Required)                ║\n"
            "║  0️⃣  Offline (Runs on your machine, no net needed)         ║\n"
            "╚══════════════════════════════════════════════════════════════╝\n"
            "👉  Type '1' for Online, or '0' for Offline: "
        )
    ),
    task: str = typer.Option(
        ...,
        prompt=(
            "\n"
            "╔══════════════════════════════════════════════════════════════════════════════╗\n"
            "║                      🚀 Choose Your Superpower Task! 🚀                     ║\n"
            "╠══════════════════════════════════════════════════════════════════════════════╣\n"
            "║ 🧠  explain             ➡️   Get instant command/code explanations         ║\n"
            "║ ⚡  generate            ➡️   Instantly create code/scripts                 ║\n"
            "║ 💻  system_info         ➡️   See your system's core details                ║\n"
            "║ 💡  dev_tips            ➡️   Wise & handy dev tips                        ║\n"
            "║ 🐳  docker_containers   ➡️   List your Docker containers                   ║\n"
            "║ 🖼️  docker_images       ➡️   Check out Docker images                       ║\n"
            "║ 🚀  docker_run          ➡️   Start a Docker container                      ║\n"
            "║ 🛑  docker_stop         ➡️   Stop a Docker container                       ║\n"
            "║ 🔍  git_status          ➡️   See your Git project status                   ║\n"
            "║ ➕  git_add             ➡️   Add files to Git (staging area)               ║\n"
            "║ 💾  git_commit          ➡️   Commit your changes to Git                    ║\n"
            "║ ⤴️  git_push            ➡️   Push code to remote repo                      ║\n"
            "║ ⤵️  git_pull            ➡️   Pull the latest from remote                   ║\n"
            "╚══════════════════════════════════════════════════════════════════════════════╝\n"
            "👑  Type exactly as shown (e.g., 'explain', 'docker_images', 'git_commit'): "
        )
    ),
):
    typer.secho("\n🔥 Let's Go! You're in {} mode. Selected task: {}".format('ONLINE 🌐' if mode else 'OFFLINE 🖥️', task), fg=typer.colors.BRIGHT_MAGENTA, bold=True)
    # ----  Place your task-handing code here  ----
    # e.g., call functions based on user's 'task'
    typer.secho("🚧 (This is where your function for '{}' would run!) 🚧".format(task), fg=typer.colors.YELLOW, bold=True)

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

    elif task == "dev_tips":
        tipsss = get_daily_tips()
        print(tipsss)
        print("\n")
        print(tipsss)

    elif  task == "docker_containers":
        show = show_containers()
        print(show)

    elif task == "docker_images":
        show = show_docker_images()
        print(show)

    elif task == "git_status":
        print(git_status())

    elif task =="git_add":
        file = typer.prompt("Enter the file to add !! ")
        print(git_add(file))


    elif task == "git_pull":
        out = git_pull()
        print(out)
    

    elif task == "git_push":
        out = git_push()
        print(out)


    elif task == "git_commit":
        message = typer.prompt("Enter the message to commit !!! ")
        print(git_commit(message))



    
    elif task == "docker_run":
        doc_image_name = typer.prompt("Enter the docker image name :)")
        runner = docker_run(doc_image_name)
        print(runner)
   
    
    elif task == "docker_stop":
        doc_stop_image_name = typer.prompt("Enter the  Image ID to Stop :)")
        stopper = docker_stop(doc_stop_image_name)
        print(stopper)

    else:
        print("task not found.. Available task [explain , generate , system_info]")



if __name__ == "__main__":
    show_banner()
    app()

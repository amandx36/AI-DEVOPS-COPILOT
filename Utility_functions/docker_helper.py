# this module help us to get the docker helpline !!! 

import subprocess       # this module is used to run the external program into my program !!!!!! 


# this is the function used to display the running docker container bro 

def show_containers():
    result =  subprocess.run(['sudo' ,'docker' ,'ps'] , capture_output = True ,  text= True)    # capture_output is used to capture the command output instead of printing it [command is subprocess ]      TEXT = True is used to convert the output that is byte  into the text 

    if result.stdout:           #stdout contain the standard output of our command as a string !!! 
        return result.stdout
    
    else:
        return "No running container found , Run first !! "
    



# function to list all the running docker images !!! 

def show_docker_images():
    result = subprocess.run(['docker','images'], capture_output = True , text= True )


    if result.stdout:
        return result.stdout

    else :
        return "No Running Docker images !! , Run First !! "
    




# this function help you to run the specific docker image !! 

def docker_run(image_name):
    try:
        result = subprocess.run(['docker', 'run', '-d', image_name], capture_output=True, text=True)
        return result.stdout or f"Container for {image_name} started."
    except Exception as e:
        return f"docker run failed: {str(e)}"

#this function help you to stop the specific docker image !! 


def docker_stop(container_id):
    try:
        result = subprocess.run(['docker', 'stop', container_id], capture_output=True, text=True)
        return result.stdout or f"Container {container_id} stopped."
    except Exception as e:
        return f"docker stop failed: {str(e)}"

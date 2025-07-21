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
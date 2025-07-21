# this module contain the function of git helper !!! 

import subprocess 



# function for the checking the file status !!! 

def git_status():
    result  = subprocess.run(['git','status'],capture_output= True , text = True)                # capture_output is used to capture the command output instead of printing it [command is subprocess ]      TEXT = True is used to convert the output that is byte  into the text 
    if result.stdout:
        return result
    else:
        return "Something Went Wrong With the git Status !!"
    


# function for adding the file into the git staging area !!! 
def git_add(file):
    try:
        result = subprocess.run(['git', 'add', file], capture_output=True, text=True)# capture_output is used to capture the command output instead of printing it [command is subprocess ]      TEXT = True is used to convert the output that is byte  into the text 

        return result.stdout or f"Added {file} to staging area bro!"
    except Exception as e:
        return f"Error adding file {file}: {str(e)}"


# this function help you  to commit your code to staging area !! 


def git_commit(msg):
    try:
        result= subprocess.run(['git','commit','-m',msg],capture_output= True , text = True)
    except  Exception as e :
        return f"commit failed: {str(e)}"
    


# this function is hep you to push the code 
def git_push():
    try:
        result = subprocess.run(['git', 'push'], capture_output=True, text=True)
        return result.stdout or "Push done."
    except Exception as e:
        return f"git push failed: {str(e)}"


# This function help you to pull the code !! 

def git_pull():
    try:
        result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
        return result.stdout or "Pull done."
    except Exception as e:
        return f"git pull failed: {str(e)}"



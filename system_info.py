#  this file is used to get the information from the system brother !! 


import psutil    # this is the library used to get the system information !!! 


def get_system_information():
    cpu_usage = psutil.cpu_percent(interval= 1)     # to get the cpu usage
    memory_usage = psutil.virtual_memory().percent        # to get the information about the memory usage 
    disk_usage = psutil.disk_usage('/').percent   # to get the disk usage 
    cpu_cores = psutil.cpu_count(logical=True)           # to get the cpu core usage !! 
   
    swap_memory = psutil.swap_memory().percent    # use to get the swap memory usage 

    information  =  f"\n \nCPU usage of your system is {cpu_usage}%, \nMemory Usage is {memory_usage}%, \nDisk usage is {disk_usage}%, \n Number of CPU cores in your system is {cpu_cores}, \n Swap memory usage is {swap_memory}%  "
    
    
    
    

    return information 
import typer 

app = typer.Typer()      # creted the obect !! 

# @app.command()       # “It is a decorator that registers the function as a CLI command so users can run it from the terminal.”
# def printing(name:str):
#     print(f"my name is {name}")


# @app.command()
# def taking_input(age :int):
#     print(f"my age is {age}")




# define the flag   using the typer options !! 


# @app.command()
# def greet(name : str , flag : bool = typer.Option(False)):   # flag !!  is just a name for the variable !
#     if excited :
#         print(f"my name is {name}")
#     else:
#         print("flag false he hai be ")


# now using the two arguments !!!! 


# @app.command()
# def product(
#     num1 :  int =typer.Argument(... , help ="Enter the first number !! "),   # Argument is used to say it is manditory 
#     num2 : int = typer.Argument(... ,help = "Enter the second number !! " )):
#     print(f"when we multiply the number {num1} with the {num2} we get the result {num1*num2}")




# now we are taking the input form the user yarr !! 


# @app.command()
# def input_taking (Enter_the_input : str= typer.Option(..., prompt =  True  ))  :
#      # option is used to take the input from the user and if you want too hide the input use hide_input = True ; while the typer.option is used to take input from the cli 
#     print(f"your input is  {Enter_the_input}")



# by using the text or the docstring !!!!

# @app.command (help = "This command greet the user by his/her name !!! ")
# def greet(name : str = typer.Argument(..., help="the name of the user !! ")):
#     print(f"The name of the user is {name}")




# now the multiple subcommands !!! 

# this work like this !!! 

# Main CLI
#  ├── greet
#  └── math
#       └── add



app = typer.Typer()         # create the main cli app 

maths_cal = typer.Typer()       # create the second cli app for the addition 

@app.command(help = "This is used to greet the command !! ")            # defining the greet under the main cli app    
def greet():                    
    print("Hello Aman deep")


@maths_cal.command(help = "This is used to calculate the mathematics !! ")              # under the maths_cli app we are defining the add 
def add(a : int , b : int):
    print(a + b)    

app.add_typer(maths_cal , name = "maths")               # .add_typer  =  function provided by Typer to add a sub-app to your main app.


if __name__ == "__main__":    # “If this file is run directly, execute the app(). If it is imported in another file, don’t run the CLI automaticall 

    app()


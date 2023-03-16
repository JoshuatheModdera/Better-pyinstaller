import time
import os
import subprocess

# Do not try to edit this code, doing so will result in a bad error and changes will not be saved
def get_dir():
    path = os.getcwd()
    files = os.listdir(path)

    for file in files:
        full_path = os.path.join(path, file)
        print(full_path)


def type(text,speed = 0.5):
    for char in text:
        print(char, end="", flush=True)      
        sleeptime = speed / 10
        time.sleep(sleeptime)
    print()


run_again = True
while run_again:
    cd = get_dir()
    type(
        "\033[34m"
        + r"""
  ____       _   _              _____       _           _        _ _  __      ____ 
 |  _ \     | | | |            |  __ \     (_)         | |      | | | \ \    / /_ |
 | |_) | ___| |_| |_ ___ _ __  | |__) |   _ _ _ __  ___| |_ __ _| | |  \ \  / / | |
 |  _ < / _ \ __| __/ _ \ '__| |  ___/ | | | | '_ \/ __| __/ _` | | |   \ \/ /  | |
 | |_) |  __/ |_| ||  __/ |    | |   | |_| | | | | \__ \ || (_| | | |    \  /   | |
 |____/ \___|\__|\__\___|_|    |_|    \__, |_|_| |_|___/\__\__,_|_|_|     \/    |_|
                                       __/ |                                       
                                      |___/                                        
    """
        + "\033[0m",speed = 0.05
    )
    type("is the file you want in the current directory? [y]/[n]:  ")
    a = input()
    a.lower()
    x = 0
    while x == 0:
        if a == "y":
            print(cd)
            break
        elif a == "n":
            try:
                os.chdir(input("What is the new directory: "))
                break
            except:
                print("Not a valid directory. Please try again.")
                x = 0
        else:
            print("Not an answer")
            break
    type("Step one now activating")
    time.sleep(0.5)
    type("Step one now active")

    fn = input("What is the file name: ")
    x = 0
    while x == 0:
        if not os.path.exists(fn) or not fn.endswith(".py"):
            type("That is not a valid file or it does not exist")
            type("NOTE: This only supports .py files")
            break
            x = 0
        else:
            type("File has been verified, time for step 2")
            time.sleep(0.5)
            type("Converting file to executable...")
            x = 1

    try:
        begining_time = time.time()
        subprocess.run(["pyinstaller", "--onefile", fn], check=True)
        type("File has been successfully converted to executable!")
        end_time = time.time()
    except subprocess.CalledProcessError:
        type("Error: Failed to convert file to executable")

    dt = time.time()
    total_time = begining_time.__floor__() - end_time.__floor__()
    total_time = f"{total_time}"
    total_time = total_time.removeprefix("-")
    type(f"This took {total_time} seconds to download {fn}")
    type("Thank you for using Better Installer")
    type("Credits to Lencano for programming and nobody lol for the idea :)")
    type("would you like to do another file? [y]/[n]: ")
    runagain = input().lower()
    d = False

    while not d:
        
        if runagain == "y":
            run_again = True
            d = True
        elif runagain == "n":
            run_again = False
            d = True
        else:
            print("Not a valid awnser try again")
            d = False
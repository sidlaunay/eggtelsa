import requests
from tkinter import Tk, messagebox
import time

IP_ADDRESS = "10.1.40.249"
USERNAME = "eggadmin"
PASSWORD = "3eggtelsa$"

def open_door():
    url = f"http://{IP_ADDRESS}/status.xml"
    params = {
        'a': f'{USERNAME}:{PASSWORD}',
        'pl1': '1'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        root = Tk()
        root.withdraw() 
        # Set the window icon
        root.iconbitmap(r'U:\05-IT\GM14-OuverturePorte\GM14-PORTE.ico') 
        messagebox.showinfo("Notification", "La porte est ouverte")
        time.after(5) 
        root.destroy()
    else:
        print("Failed to open the door. Status code:", response.status_code)

if __name__ == "__main__":
    open_door()
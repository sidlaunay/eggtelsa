import requests
from tkinter import Tk, messagebox
import time

# Définir les variables pour l'adresse IP, l'utilisateur et le mot de passe
IP_ADDRESS = "10.1.40.39"
USERNAME = "admin"
PASSWORD = "admin"

def open_door():
    url = f"http://{IP_ADDRESS}/status.xml"
    params = {
        'a': f'{USERNAME}:{PASSWORD}',
        'pl1': '1'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        root = Tk()
        root.withdraw()  # Hiding the main window
        messagebox.showinfo("Notification", "La porte est ouverte")
        time.sleep(5)  # Attendre 5 secondes avant de fermer la fenêtre
        root.destroy()
    else:
        print("Failed to open the door. Status code:", response.status_code)

if __name__ == "__main__":
    open_door()

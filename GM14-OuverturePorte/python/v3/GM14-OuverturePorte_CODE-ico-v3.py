import requests
from tkinter import Tk, messagebox

IP_ADDRESS = "10.1.40.249"
USERNAME = "eggadmin"
PASSWORD = "3eggtelsa$"

def open_door():
    url = f"http://{IP_ADDRESS}/status.xml"
    params = {
        'a': f'{USERNAME}:{PASSWORD}',
        'pl1': '1'
    }
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            root = Tk()
            root.withdraw()  # Cache la fenêtre principale
            root.iconbitmap(r'U:\05-IT\GM14-OuverturePorte\GM14-PORTE.ico')  # Définit l'icône de la fenêtre
            messagebox.showinfo("Notification", "La porte est ouverte")
            root.after(5000, root.destroy)  # Programme la fermeture de la fenêtre après 5000 ms (5 secondes)
            root.mainloop()  # Démarre la boucle principale de Tkinter pour que la fenêtre reste ouverte
        else:
            print("Failed to open the door. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error connecting to device:", e)

if __name__ == "__main__":
    open_door()

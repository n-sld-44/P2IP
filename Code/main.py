
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 18:01:06 2024

@author: maria
"""

import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import shutil
from PIL import Image, ImageTk
#from moviepy.editor import VideoFileClip
import cv2
import tkinter.ttk as ttk 
import lemmma
from speach_to_text import speach_to_text
from movie_clip import parsed_to_clip
def select_video():
    file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov")])
    if file_path:
        destination_path = r".\Files\video\video.mp4"  # Spécifiez votre chemin d'accès de destination ici
        try:
            shutil.copyfile(file_path, destination_path)
            label_file_path.config(text="La vidéo a été enregistrée avec succès.", fg="green")
            #response = messagebox.askyesno( "Souhaitez-vous afficher la vidéo ?")
                
            

            response = custom_yesno_dialog("Souhaitez-vous traduire la vidéo avec un overlay en LSF?")
            if response:
                
                show_video(r"./Files/video/video_finale.mp4")
        except Exception as e:
            label_file_path.config(text="Erreur lors de l'enregistrement de la vidéo : " + str(e), fg="red")
            

def custom_yesno_dialog(message): #permet d'afficher la fenêtre qui demande à l'utilisateur s'il souhaite visionner la vidéo
    
    response = [False]  # Utiliser une liste pour pouvoir la modifier dans les sous-fonctions
    
    def on_yes():
        response[0] = True
        text = speach_to_text()
        parsed = lemmma.parse(text)
        parsed_to_clip(parsed)
        dialog.destroy()
    
    def on_no():
        response[0] = False
        dialog.destroy()
    
    dialog = tk.Toplevel()
    dialog.title("Confirmation")
    dialog.iconphoto(False,logo)
    
    label = tk.Label(dialog, text=message)
    label.pack(padx=20, pady=10)

    yes_button = tk.Button(dialog, text="Oui", command=on_yes)
    yes_button.pack(side="left", padx=10, pady=10)

    no_button = tk.Button(dialog, text="Non", command=on_no)
    no_button.pack(side="right", padx=10, pady=10)

    dialog.focus_set()
    dialog.grab_set()
    dialog.wait_window()
    
    return response[0]


def show_video(video_path):
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video',frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()

      
            
# Définit la taille de la fenêtre   
root = tk.Tk()
root.title("SignTrad")
root.state('zoomed')  

logo = PhotoImage(file='./Files/images_interface/logo.png')
root.iconphoto(False, logo)
# Création d'un canevas (Canvas) pour le fond d'écran bleu marine
canvas = tk.Canvas(root, width=1000, height=600, bg="white")
canvas.pack(expand=True, fill="both")  # Le canevas s'étend pour remplir toute la fenêtre

# Chargement de l'image et conversion en ImageTk
image_path = r"./Files/images_interface/Interface.png"
image = Image.open(image_path)
image = image.resize((1500, 1100))
photo = ImageTk.PhotoImage(image)

# Création du label avec l'image et placement sur le canevas
label_image = tk.Label(canvas, image=photo, bg="white")
label_image.pack(expand = True)

# Création d'une frame pour afficher les messages
message_frame = tk.Frame(root, bg="white")
message_frame.place(relx=0.5, rely=0.9, anchor="center", relwidth=0.8, relheight=0.1)

# Label pour afficher le chemin du fichier sélectionné et placement sur le canevas
label_file_path = tk.Label(message_frame, text="", bg="white", fg="black")
label_file_path.pack(expand = True)

# Appliquer un style au bouton
style = ttk.Style()
style.configure("TButton",
                font=("Helvetica", 14),  # Taille de l'écriture
                padding=40,  # Padding pour augmenter la taille du bouton
                relief="flat",  # Suppression des bordures natives
                background="white",  # Couleur de fond du bouton
                foreground="black")  # Couleur du texte

# Remplacer le bouton par un bouton TTK avec style personnalisé
select_button = ttk.Button(root, text="Démarrer", command=select_video, style="TButton")
select_button.place(relx=0.75, rely=0.5, anchor='center')


root.mainloop()

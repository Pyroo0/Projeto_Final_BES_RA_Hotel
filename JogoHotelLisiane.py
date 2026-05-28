import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk

hotel = tk.Tk()
hotel.title("Gestão de Pousada")
hotel.geometry("700x900")
hotel.grid_columnconfigure(0, weight=1)

imagem_original = Image.open("pixel-art-hotel.jpg")
imagem_redimensionada = imagem_original.resize((250, 250))
imagem_tk = ImageTk.PhotoImage(imagem_redimensionada)
label_imagem = tk.Label(image=imagem_tk)
label_imagem.pack(pady=20)

label_chkin = tk.Label(hotel, text="Check-in Hóspedes", anchor="w", font=("Arial", 12))
label_chkin.pack(fill="x", padx=30, pady=10)
label_hospede = tk.Label(hotel, text="Nome do hóspede:", anchor="w", font=("Arial", 10))
label_hospede.pack(fill="x", padx=30, pady=5)
entry_nome = tk.Entry(hotel)
entry_nome.pack( anchor="w", padx=30, pady=5)



hotel.mainloop()
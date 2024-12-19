import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip
import os

Suprimir advertencias de Tkinter en macOS
os.environ['TK_SILENCE_DEPRECATION'] = '1'

Función para generar la contraseña
def generate_password():
length = int(length_slider.get())
characters = ""
if use_uppercase.get():
characters += string.ascii_uppercase
if use_lowercase.get():
characters += string.ascii_lowercase
if use_numbers.get():
characters += string.digits
if use_special.get():
characters += string.punctuation
if characters:
password = '’.join(random.choice(characters) for _ in range(length))
password_var.set(password)
check_strength(password)
else:
password_var.set("Selecciona al menos una opción")
strength_var.set("")

Función para verificar la seguridad de la contraseña
def check_strength(password):
strength = 0
if len(password) >= 12:
strength += 1
if any(char.isdigit() for char in password):
strength += 1
if any(char.isupper() for char in password):
strength += 1
if any(char.islower() for char in password):
strength += 1
if any(char in string.punctuation for char in password):
strength += 1

if strength == 5:
    strength_var.set("Muy segura")
elif strength >= 3:
    strength_var.set("Segura")
else:
    strength_var.set("Poco segura")
Copiar contraseña al portapapeles
def copy_password():
password = password_var.get()
if password and password != "Selecciona al menos una opción":
pyperclip.copy(password)
status_var.set("Contraseña copiada al portapapeles")
else:
status_var.set("No hay contraseña para copiar")

Actualizar la longitud de la contraseña
def update_length(value):
length_var.set(f"Longitud: {int(float(value))}")

Crear la ventana principal
window = tk.Tk()
window.title("Generador de Contraseñas")
window.geometry("400x550")
window.configure(bg="#1F2A36")

Crear un frame
frame = tk.Frame(window, bg="#1F2A36", bd=5)
frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

Variables
password_var = tk.StringVar()
strength_var = tk.StringVar()
length_var = tk.StringVar()
status_var = tk.StringVar()
use_uppercase = tk.BooleanVar(value=True)
use_lowercase = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

Título
title = tk.Label(frame, text="Generador de Contraseñas", font=("Helvetica", 18, "bold"), fg="white", bg="#1F2A36")
title.pack(pady=10)

Entry para mostrar la contraseña generada
entry_password = tk.Entry(frame, textvariable=password_var, state=’readonly’, font=("Helvetica", 14), width=32)
entry_password.pack(pady=10)

Etiqueta para la fuerza de la contraseña
label_strength = tk.Label(frame, textvariable=strength_var, font=("Helvetica", 12, "italic"), fg="white", bg="#1F2A36")
label_strength.pack(pady=5)

Slider para la longitud de la contraseña
length_label = tk.Label(frame, textvariable=length_var, font=("Helvetica", 12), fg="white", bg="#1F2A36")
length_label.pack(pady=5)
length_slider = ttk.Scale(frame, from_=5, to=64, orient=tk.HORIZONTAL, length=300, command=update_length)
length_slider.set(12)
length_slider.pack(pady=10)
update_length(12) # Inicializar la etiqueta de longitud

Opciones de caracteres
tk.Checkbutton(frame, text="Mayúsculas", variable=use_uppercase, bg="#1F2A36", fg="white", selectcolor="#6C7A89").pack(anchor=’w’, padx=20)
tk.Checkbutton(frame, text="Minúsculas", variable=use_lowercase, bg="#1F2A36", fg="white", selectcolor="#6C7A89").pack(anchor=’w’, padx=20)
tk.Checkbutton(frame, text="Números", variable=use_numbers, bg="#1F2A36", fg="white", selectcolor="#6C7A89").pack(anchor=’w’, padx=20)
tk.Checkbutton(frame, text="Especiales", variable=use_special, bg="#1F2A36", fg="white", selectcolor="#6C7A89").pack(anchor=’w’, padx=20)

Botón para generar contraseña
generate_button = tk.Button(frame, text="Generar Contraseña", command=generate_password, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white")
generate_button.pack(pady=10)

Botón para copiar contraseña
copy_button = tk.Button(frame, text="Copiar", command=copy_password, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white")
copy_button.pack(pady=10)

Etiqueta de estado
status_label = tk.Label(frame, textvariable=status_var, font=("Helvetica", 10), fg="white", bg="#1F2A36")
status_label.pack(pady=5)

Ejecutar ventana
window.mainloop()
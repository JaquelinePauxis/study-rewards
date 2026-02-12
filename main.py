import tkinter as tk
from tkinter import messagebox

def calcular_pontos():
    try:
        minutos = int(entry_minutos.get())
        # Regra: 10 pontos a cada 25 minutos
        pontos = (minutos // 25) * 10
        
        if pontos > 0:
            resultado_label.config(text=f"Você ganhou {pontos} cristais! 💎", fg="#2ecc71")
        else:
            resultado_label.config(text="Continue estudando para ganhar cristais!", fg="#e67e22")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números inteiros.")

# Configuração da Janela
janela = tk.Tk()
janela.title("Study Rewards")
janela.geometry("400x300")
janela.configure(bg="#2c3e50")

# UI
titulo = tk.Label(janela, text="Foco no Código! 🐍", font=("Arial", 18, "bold"), bg="#2c3e50", fg="#ecf0f1")
titulo.pack(pady=20)

instrucao = tk.Label(janela, text="Quantos minutos você estudou?", bg="#2c3e50", fg="#bdc3c7")
instrucao.pack()

entry_minutos = tk.Entry(janela, font=("Arial", 14), justify="center")
entry_minutos.pack(pady=10)

botao_calcular = tk.Button(janela, text="Resgatar Pontos", command=calcular_pontos, 
                           bg="#3498db", fg="white", font=("Arial", 12, "bold"))
botao_calcular.pack(pady=10)

resultado_label = tk.Label(janela, text="", bg="#2c3e50", font=("Arial", 12, "bold"))
resultado_label.pack(pady=20)

janela.mainloop()
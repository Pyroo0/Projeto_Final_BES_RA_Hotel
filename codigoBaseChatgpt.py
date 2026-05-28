import tkinter as tk
from tkinter import messagebox
import datetime
import random

# Constantes
VALOR_DIARIA = 150.00
LIMITE_QUARTOS = 5

# Variáveis principais
faturamento_diario = 0.0
quartos = [None] * LIMITE_QUARTOS
historico = []

# Dicionário de produtos
produtos = {
    "Água": 5.0,
    "Refrigerante": 8.0,
    "Cerveja": 12.0,
    "Snack": 10.0
}

# Funções
def realizar_checkin():
    nome = entry_nome.get()
    dias = entry_dias.get()
    if not nome or not dias.isdigit():
        messagebox.showwarning("Erro", "Preencha nome e dias corretamente!")
        return
    dias = int(dias)
    for i in range(LIMITE_QUARTOS):
        if quartos[i] is None:
            reserva_id = random.randint(1000, 9999)
            quartos[i] = {"nome": nome, "dias": dias, "consumo": 0.0, "reserva": reserva_id}
            messagebox.showinfo("Check-in", f"{nome} hospedado no quarto {i+1}. Reserva #{reserva_id}")
            atualizar_status()
            return
    messagebox.showwarning("Lotado", "Não há quartos disponíveis!")

def registrar_consumo():
    quarto = entry_quarto.get()
    item = combo_produto.get()
    if not quarto.isdigit():
        messagebox.showwarning("Erro", "Digite o número do quarto!")
        return
    quarto = int(quarto) - 1
    if 0 <= quarto < LIMITE_QUARTOS and quartos[quarto] is not None:
        if item in produtos:
            quartos[quarto]["consumo"] += produtos[item]
            messagebox.showinfo("Consumo", f"{item} registrado - R${produtos[item]:.2f}")
        else:
            messagebox.showwarning("Erro", "Produto inválido!")
    else:
        messagebox.showwarning("Erro", "Quarto não ocupado!")
    atualizar_status()

def calcular_checkout():
    global faturamento_diario
    quarto = entry_quarto.get()
    if not quarto.isdigit():
        messagebox.showwarning("Erro", "Digite o número do quarto!")
        return
    quarto = int(quarto) - 1
    if 0 <= quarto < LIMITE_QUARTOS and quartos[quarto] is not None:
        hospede = quartos[quarto]
        valor_estadia = hospede["dias"] * VALOR_DIARIA
        total = valor_estadia + hospede["consumo"]
        faturamento_diario += total
        historico.append(f"{hospede['nome']} - R${total:.2f}")
        messagebox.showinfo("Checkout", f"{hospede['nome']} pagou R${total:.2f}")
        quartos[quarto] = None
    else:
        messagebox.showwarning("Erro", "Quarto não ocupado!")
    atualizar_status()

def atualizar_status():
    texto = ""
    for i, q in enumerate(quartos, start=1):
        if q is None:
            texto += f"Quarto {i}: Livre\n"
        else:
            texto += f"Quarto {i}: {q['nome']} (Reserva #{q['reserva']})\n"
    label_status.config(text=texto)

def encerrar_sistema():
    data = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    with open("relatorio.txt", "w", encoding="utf-8") as f:
        f.write(f"Relatório de {data}\n")
        f.write(f"Faturamento total: R${faturamento_diario:.2f}\n")
        f.write("Histórico de estadias:\n")
        for h in historico:
            f.write(h + "\n")
    messagebox.showinfo("Encerrado", "Relatório salvo em relatorio.txt\nSistema encerrado.")
    root.quit()

# Interface Tkinter
root = tk.Tk()
root.title("Gestão de Pousada")
root.geometry("500x500")

# Check-in
tk.Label(root, text="Nome do hóspede:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()
tk.Label(root, text="Dias de estadia:").pack()
entry_dias = tk.Entry(root)
entry_dias.pack()
tk.Button(root, text="Fazer Check-in", command=realizar_checkin).pack(pady=5)

# Consumo
tk.Label(root, text="Número do quarto:").pack()
entry_quarto = tk.Entry(root)
entry_quarto.pack()
tk.Label(root, text="Produto consumido:").pack()
combo_produto = tk.StringVar(root)
combo_produto.set("Água")
tk.OptionMenu(root, combo_produto, *produtos.keys()).pack()
tk.Button(root, text="Registrar Consumo", command=registrar_consumo).pack(pady=5)

# Checkout
tk.Button(root, text="Fazer Check-out", command=calcular_checkout).pack(pady=5)

# Status
label_status = tk.Label(root, text="Status dos quartos aparecerá aqui", justify="left")
label_status.pack(pady=10)

# Encerrar
tk.Button(root, text="Encerrar Sistema", command=encerrar_sistema, bg="red", fg="white").pack(pady=10)

root.mainloop()

# interface.py - define a interface gráfica tkinter
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from database import inserir_compra, listar_compras

def iniciar_interface():
    def adicionar():
        inserir_compra(entry_nome.get(), entry_nota.get(), entry_qtd.get(), entry_valor.get(), entry_data.get())
        atualizar_tabela()
        limpar()

    def atualizar_tabela():
        for item in tree.get_children():
            tree.delete(item)
        for row in listar_compras():
            tree.insert("", "end", values=row)

    def limpar():
        entry_nome.delete(0, tk.END)
        entry_nota.delete(0, tk.END)
        entry_qtd.delete(0, tk.END)
        entry_valor.delete(0, tk.END)
        entry_data.delete(0, tk.END)
        entry_data.insert(0, datetime.now().strftime("%Y-%m-%d"))

    janela = tk.Tk()
    janela.title("Financeiro TI")
    janela.geometry("800x500")
    janela.configure(bg="#800000")

    frame = tk.Frame(janela, bg="#800000")
    frame.pack(pady=10)

    tk.Label(frame, text="Nome", fg="white", bg="#800000").grid(row=0, column=0)
    entry_nome = tk.Entry(frame)
    entry_nome.grid(row=0, column=1)

    tk.Label(frame, text="Nota", fg="white", bg="#800000").grid(row=1, column=0)
    entry_nota = tk.Entry(frame)
    entry_nota.grid(row=1, column=1)

    tk.Label(frame, text="Quantidade", fg="white", bg="#800000").grid(row=0, column=2)
    entry_qtd = tk.Entry(frame)
    entry_qtd.grid(row=0, column=3)

    tk.Label(frame, text="Valor", fg="white", bg="#800000").grid(row=1, column=2)
    entry_valor = tk.Entry(frame)
    entry_valor.grid(row=1, column=3)

    tk.Label(frame, text="Data Recebimento", fg="white", bg="#800000").grid(row=2, column=0)
    entry_data = tk.Entry(frame)
    entry_data.insert(0, datetime.now().strftime("%Y-%m-%d"))
    entry_data.grid(row=2, column=1)

    btn_add = tk.Button(janela, text="Adicionar Compra", command=adicionar, bg="#a52a2a", fg="white")
    btn_add.pack(pady=10)

    tree = ttk.Treeview(janela, columns=("Nome", "Nota", "Qtd", "Valor", "Data"), show="headings")
    tree.heading("Nome", text="Nome")
    tree.heading("Nota", text="Nota")
    tree.heading("Qtd", text="Qtd")
    tree.heading("Valor", text="Valor")
    tree.heading("Data", text="Data")
    tree.pack(fill="both", expand=True)

    atualizar_tabela()
    janela.mainloop()

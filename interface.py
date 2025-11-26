import tkinter as tk
from tkinter import simpledialog, messagebox
from backend import AtalhosBackend

class AppInterface:
    def __init__(self):
        self.backend = AtalhosBackend()

        self.root = tk.Tk()
        self.root.title("Gerenciador de Atalhos")
        self.root.geometry("400x400")

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Adicionar Atalho", command=self.adicionar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Remover Selecionado", command=self.remover).pack(side=tk.LEFT, padx=5)

        self.lista = tk.Listbox(self.root, width=50, height=20)
        self.lista.pack(pady=10)

        self.atualizar_lista()

    def adicionar(self):
        atalho = simpledialog.askstring("Novo Atalho", "Digite o atalho:")
        if not atalho:
            return

        descricao = simpledialog.askstring("Descrição", "Digite a descrição:")
        if not descricao:
            return

        self.backend.adicionar(atalho, descricao)
        self.atualizar_lista()
        messagebox.showinfo("Ok", "Atalho salvo!")

    def remover(self):
        selecionado = self.lista.curselection()
        if not selecionado:
            return
        
        linha = self.lista.get(selecionado[0])
        atalho = linha.split(" → ")[0]

        if self.backend.remover(atalho):
            self.atualizar_lista()
            messagebox.showinfo("OK", "Removido!")

    def atualizar_lista(self):
        self.lista.delete(0, tk.END)
        for atalho, desc in self.backend.listar().items():
            self.lista.insert(tk.END, f"{atalho} → {desc}")

    def run(self):
        self.root.mainloop()

import tkinter as tk
from tkinter import simpledialog, messagebox
from backend import AtalhosBackend

class AppInterface:
    def __init__(self):
        self.backend = AtalhosBackend()

        self.root = tk.Tk()
        self.root.title("Gerenciador de Atalhos")
        self.root.geometry("420x460")

        # --------------------------
        # Campo de busca
        # --------------------------
        tk.Label(self.root, text="Pesquisar:").pack(pady=(10, 0))
        self.entrada_busca = tk.Entry(self.root, width=40)
        self.entrada_busca.pack()
        self.entrada_busca.bind("<KeyRelease>", self.filtrar_lista)

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Button(frame, text="Adicionar Atalho", command=self.adicionar).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Remover Selecionado", command=self.remover).pack(side=tk.LEFT, padx=5)

        self.lista = tk.Listbox(self.root, width=55, height=20)
        self.lista.pack(pady=10)

        self.atualizar_lista()

    # --------------------------
    # Ações
    # --------------------------

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

    # --------------------------
    # Listagem normal + filtrada
    # --------------------------

    def atualizar_lista(self):
        self.mostrar_lista(self.backend.listar())

    def filtrar_lista(self, event=None):
        texto = self.entrada_busca.get()
        if texto.strip() == "":
            self.atualizar_lista()
        else:
            filtrados = self.backend.buscar(texto)
            self.mostrar_lista(filtrados)

    def mostrar_lista(self, dados):
        self.lista.delete(0, tk.END)
        for atalho, desc in dados.items():
            self.lista.insert(tk.END, f"{atalho} → {desc}")

    def run(self):
        self.root.mainloop()

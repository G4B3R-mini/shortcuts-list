from database import carregar_atalhos, salvar_atalhos

class AtalhosBackend:
    def __init__(self):
        self.atalhos = carregar_atalhos()

    def listar(self):
        return self.atalhos

    def adicionar(self, atalho, descricao):
        self.atalhos[atalho] = descricao
        salvar_atalhos(self.atalhos)

    def remover(self, atalho):
        if atalho in self.atalhos:
            self.atalhos.pop(atalho)
            salvar_atalhos(self.atalhos)
            return True
        return False

    def buscar(self, texto):
        texto = texto.lower()
        return {
            atalho: desc
            for atalho, desc in self.atalhos.items()
            if texto in atalho.lower() or texto in desc.lower()
        }

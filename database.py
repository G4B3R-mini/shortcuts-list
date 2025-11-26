import json
import os

ARQUIVO = "atalhos.json"

def carregar_atalhos():
    if os.path.exists(ARQUIVO):
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {}
    return {}

def salvar_atalhos(atalhos: dict):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(atalhos, f, indent=4, ensure_ascii=False)

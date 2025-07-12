import os
from dotenv import load_dotenv
from api.gemini import gerar_redacao
from utils.gerador_pdf import salvar_redacao_pdf

load_dotenv()

caminho = os.path.expanduser("~/Documentos/Redações")

os.makedirs(caminho, exist_ok=True)

tipo = input("Digite o tipo de redação (Ex: Dissertação, Carta, Crônica): ")
tema = input("Digite o tema da redação: ")

prompt = f"Escreva uma redação do tipo {tipo} sobre o tema: {tema} em português. Deve ter entre 20 e 30 linhas. Contendo introdução, desenvolvimento e conclusão, seguindo as normas da ABNT exigidas para redações do ENEM."

print("Gerando redação no Gemini...")
texto = gerar_redacao(prompt)

nome_pdf = salvar_redacao_pdf(texto, tema, caminho)

print(f"Redação Salva como: {nome_pdf}")
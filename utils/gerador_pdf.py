from fpdf import FPDF
import os
import re

def limpar_texto(texto: str) -> str:
    
    texto_sem_markdown = re.sub(r'(\*|_|#)', '', texto)
    return texto_sem_markdown

def salvar_redacao_pdf(texto: str, tema: str, caminho: str = ".") -> str:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    texto_limpo = limpar_texto(texto)

    for linha in texto_limpo.split('\n'):
        linha_decodificada = linha.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, linha_decodificada)

    tema_formatado = re.sub(r'[^a-zA-Z0-9_]', '', tema.replace(" ", "_"))
    nome_arquivo = f"redacao_{tema_formatado}.pdf"
    caminho_completo = os.path.join(caminho, nome_arquivo)

    try:
        pdf.output(caminho_completo)
        return caminho_completo
    except Exception as e:
        print(f"Erro ao salvar o PDF: {e}")
        return f"Erro ao salvar o PDF: {e}"
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def gerar_redacao(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return "Erro: API key do Gemini não encontrada."

    genai.configure(api_key=api_key)

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash") 
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("Erro ao gerar redação:", str(e))
        return "Erro ao gerar redação"
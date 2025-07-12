<div align="center">
  <img src="https://img.icons8.com/color/96/000000/google-logo.png" width="50"/>
  <img src="https://img.icons8.com/color/96/artificial-intelligence.png" width="50"/>
  <h1 style="color:#2d2d2d;">📝 Redação com Gemini API</h1>
  <p style="font-size:18px; color:#444;">
    Geração automática de redações no formato ENEM usando IA do Google Gemini.
  </p>
</div>

<hr/>

<h2>🚀 Funcionalidades</h2>
<ul>
  <li>🤖 <b>Geração de Redações</b> com introdução, desenvolvimento e conclusão</li>
  <li>📄 <b>Formato ABNT/ENEM</b> estruturado para o padrão do ENEM</li>
  <li>📤 <b>Exportação para PDF</b> com salvamento automático</li>
  <li>🔐 <b>Segurança com variáveis de ambiente</b> (.env)</li>
</ul>

<h2>📁 Estrutura do Projeto</h2>

<pre>
REDCACAO-GEMINI/
├── api/
│   └── gemini.py             # Interação com API Gemini
├── utils/
│   └── gerador_pdf.py        # Geração de PDFs
├── main.py                   # Script principal
├── requirements.txt          # Dependências
├── .env                      # Variáveis de ambiente
└── .gitignore                # Arquivos ignorados
</pre>

<h2>⚙️ Como Usar</h2>

<h4>📌 Pré-requisitos:</h4>
<ul>
  <li>Python 3.8 ou superior</li>
  <li>Conta no <a href="https://aistudio.google.com/" target="_blank">Google AI Studio</a> com chave da API Gemini</li>
</ul>

<h4>📥 Instalação:</h4>

<pre>
git clone https://github.com/seuusuario/redacao-gemini.git
cd redacao-gemini
pip install -r requirements.txt
</pre>

<h4>🔐 Configuração:</h4>
Crie um arquivo <code>.env</code> com:
<pre>
GEMINI_API_KEY=SUA_API_KEY_AQUI
</pre>

<h4>▶️ Execução:</h4>
<pre>
python main.py
</pre>

<h4>📂 Saída:</h4>
A redação será salva em:
<ul>
  <li><b>Linux/macOS:</b> ~/Documentos/Redações</li>
  <li><b>Windows:</b> C:\Users\SeuUsuario\Documents\Redações</li>
</ul>

<h2>🧠 Tecnologias Usadas</h2>
<ul>
  <li>Python 3.8+</li>
  <li>Google Gemini API (model: gemini-1.5-flash)</li>
  <li>dotenv</li>
  <li>fpdf</li>
</ul>

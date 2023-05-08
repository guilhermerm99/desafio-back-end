**Desafio Back-End**
### **Requisitos:**
- Python 3.x instalado (versão recomendada: 3.6 ou superior)
- Bibliotecas necessárias instaladas. Você pode instalar as dependências executando o comando **pip install -r requirements.txt**, onde o arquivo **requirements.txt** contém as bibliotecas necessárias, como **requests**, **sqlite3** e **googletrans**.

Passos para executar o projeto:

1. Faça o download do código-fonte do projeto em um diretório de sua escolha.
2. Abra um terminal ou prompt de comando e navegue até o diretório em que o código-fonte foi baixado.
3. Crie um ambiente virtual (opcional, se não achar necessário, pode pular para o 5º passo) para isolar as dependências do projeto. Para criar um ambiente virtual, execute o seguinte comando no terminal:

python -m venv env

4. Ative o ambiente virtual. Dependendo do sistema operacional e do shell, o comando pode variar:
- No Windows (cmd):

env\Scripts\activate.bat

- No Windows (PowerShell):

.\env\Scripts\Activate.ps1

- No Linux ou macOS:

source env/bin/activate

5. Instale as dependências do projeto executando o seguinte comando:

pip install -r requirements.txt

6. Após a instalação das dependências, você está pronto para executar o projeto. No terminal, execute o seguinte comando:

python main.py

7. O projeto começará a ser executado. Ele fará uma requisição HTTP para obter dados de produtos, calculará a média de preços dos smartphones, salvará os produtos no banco de dados e exibirá uma piada sobre Chuck Norris (se disponível).

Certifique-se de ter uma conexão com a internet ativa, pois o projeto depende do acesso a recursos externos, como a API de produtos e a API de piadas do Chuck Norris.

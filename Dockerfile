# Imagem base
FROM python:3.9-slim-bullseye

# Define o diretório de trabalho dentro do container
WORKDIR /workplace

# Copia os arquivos de requisitos primeiro para aproveitar o cache da camada
COPY . /workplace

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Instala o Jupyter Notebook
RUN pip install notebook
# Copia o resto dos arquivos do projeto para o diretório de trabalho

# Inicia o Bash quando o container é iniciado
#CMD ["/bin/bash"]

# Comando para executar a aplicação
CMD ["python3", "/workplace/tests/simulation/chat_simulator.py"]
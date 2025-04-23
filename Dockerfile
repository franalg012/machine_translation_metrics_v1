FROM python:3.10-slim

# Instalar git y otras dependencias del sistema 
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# carpeta de trabajo
WORKDIR /machine_learning_metrics

# Copiar
COPY . .

# Instalar las dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# NLTK
RUN python -m nltk.downloader punkt wordnet omw-1.4

# Puerto FastAPI
EXPOSE 8000

# iniciar la API con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
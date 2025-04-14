# Imagen base 
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . .

# Instalar las dependencias
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# descargar nltk para meteor
RUN python -m nltk.downloader punkt wordnet omw-1.4

# Expose the port
EXPOSE 8000

# Comando para iniciar la API con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

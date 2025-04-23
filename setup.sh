#!/bin/bash

# =============================================
# CONFIGURADOR DE PROYECTO DE MÉTRICAS DE TRADUCCIÓN
# =============================================

echo -e "\n\033[1;36m[INICIO] Configuración del proyecto...\033[0m\n"

# ---------------------------------------------
# 1. Instalar dependencias del sistema
# ---------------------------------------------
echo -e "\033[1;33m[PASO 1/4] Instalando dependencias del sistema...\033[0m"
sudo apt-get update && sudo apt-get install -y \
    python3-venv \
    python3-dev \
    build-essential \
    > /dev/null 2>&1

echo -e "  ✅ Dependencias del sistema instaladas\n"

# ---------------------------------------------
# 2. Crear y activar entorno virtual
# ---------------------------------------------
echo -e "\033[1;33m[PASO 2/4] Configurando entorno virtual...\033[0m"
python3 -m venv venv
source venv/bin/activate

echo -e "  ✅ Entorno virtual creado y activado\n"

# ---------------------------------------------
# 3. Instalar dependencias de Python
# ---------------------------------------------
echo -e "\033[1;33m[PASO 3/4] Instalando dependencias de Python...\033[0m"
pip install --upgrade pip
pip install -r requirements.txt

echo -e "  ✅ Dependencias de Python instaladas\n"

# ---------------------------------------------
# 4. Descargar recursos y modelos
# ---------------------------------------------
echo -e "\033[1;33m[PASO 4/4] Descargando modelos y recursos...\033[0m"
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet')" > /dev/null 2>&1
python -c "from comet import download_model; download_model('Unbabel/XCOMET-XL')" > /dev/null 2>&1

echo -e "  ✅ Modelos descargados\n"


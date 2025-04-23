# 🌍 Translation Metrics API

API para comparar métricas de traducción automática: <br>
 Métricas estadísticas: **BLEU**, **METEOR**, **ROUGE**, <br>
 Métricas basadas en modelos: **COMET**, **BLEURT**. <br>

---

## ⚙️ Instalación

```bash

1. Crear entorno virtual (recomendado por dependencias):
   python -m venv venv

2. Activar entorno:
   - En Windows:
     venv\Scripts\activate
   - En Unix/macOS:
     source venv/bin/activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Ejecutar el servidor:
   python main.py

```

## 🚀 Uso de la API
1. Abrir Postman.

2. Apuntar a: http://localhost:8000/evaluate

3. Método: POST

4. En el body, usar el siguiente JSON:


{
  "pairs": [
    {
      "source_text": "Hello world",
      "translated_text": "Hola mundo"
    },
    {
      "source_text": "How are you?",
      "translated_text": "¿Cómo estás?"
    }
  ],
  "metrics": ["bleu", "meteor", "rougeL", "comet", "bleurt"]
}


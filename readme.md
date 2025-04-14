# Translation Metrics API

API para comparar métricas de traducción automática (BLEU, METEOR, ROUGE, COMET, BLEURT).

## Instalación
1. Crear entorno virtual: `python -m venv venv`
2. Activar entorno: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Unix)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Ejecutar: `python main.py`

## Uso
- Endpoint: POST `/evaluate`
- Body:
```json



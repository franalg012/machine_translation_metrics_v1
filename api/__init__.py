# api/__init__.py
from .routes import router

__all__ = ["router"]  # Opcional: controla qué se exporta con `from api import *`
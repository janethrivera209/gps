import os
from pathlib import Path

DIRECTORIO_BASE = Path(__file__).resolve().parent


class Configuracion:
    """Configuración central del proyecto."""

    CLAVE_API_GOOGLE = os.getenv("CLAVE_API_GOOGLE", "AIzaSyBI7-JK1Ll0OQGwG7n0tTdkQAYRDN4f094")

    # Vehículo por defecto
    TIPO_VEHICULO_PREDETERMINADO = "CAR"

    # Combustibles
    PRECIO_GASOLINA_MXN = 23.99
    PRECIO_DIESEL_MXN = 26.50

    # Rendimientos sugeridos
    RENDIMIENTO_AUTO_KM_L = 14.0
    RENDIMIENTO_MOTO_KM_L = 32.0
    RENDIMIENTO_CAMION_KM_L = 4.5

    # Valor mostrado al iniciar
    RENDIMIENTO_PREDETERMINADO_KM_L = 14.0

    ARCHIVO_ZONAS = DIRECTORIO_BASE / "data" / "zonas_rojas.json"
    TIEMPO_ESPERA_GOOGLE_SEGUNDOS = 35

    SERVIDOR = "0.0.0.0"
    PUERTO = int(os.getenv("PORT", 5000))
    DEPURACION = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    JSON_SORT_KEYS = False
    JSON_AS_ASCII = False
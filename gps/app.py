from flask import Flask
from gps.configuracion import Configuracion
from gps.routes import registrar_rutas


def crear_aplicacion(configuracion_prueba=None):
    aplicacion = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
    )
    aplicacion.config.from_object(Configuracion)

    if configuracion_prueba:
        aplicacion.config.update(configuracion_prueba)

    registrar_rutas(aplicacion)
    return aplicacion


app = crear_aplicacion()


if __name__ == "__main__":
    app.run(
        host=app.config["SERVIDOR"],
        port=app.config["PUERTO"],
        debug=app.config["DEPURACION"],
    )

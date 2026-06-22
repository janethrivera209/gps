# Guía de Despliegue en Render

## Pasos para desplegar tu aplicación GPS en Render:

### 1. **Preparar el repositorio en GitHub**
```bash
git init
git add .
git commit -m "Preparar para despliegue en Render"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

### 2. **Crear una cuenta en Render**
- Ve a https://render.com
- Regístrate con tu cuenta de GitHub
- Autoriza Render para acceder a tus repositorios

### 3. **Desplegar desde Render Dashboard**
1. En Render, haz clic en **"New +"** → **"Web Service"**
2. Conecta tu repositorio de GitHub
3. Render detectará automáticamente el archivo `render.yaml`
4. Configura las variables de entorno:
   - `CLAVE_API_GOOGLE`: Tu clave de API de Google Maps

### 4. **Configurar variables de entorno**
Antes de desplegar, ve a **Environment**:
1. Copia tu clave de API de Google
2. Crea una variable llamada `CLAVE_API_GOOGLE` con tu clave
3. Deja las demás como están

### 5. **Verificar el despliegue**
- Render proporcionará una URL como: `https://gps-automatas-xxxx.onrender.com`
- Accede a ella para verificar que la aplicación funciona

## Variables de entorno requeridas:
- `CLAVE_API_GOOGLE`: Tu clave de API de Google Maps (obligatorio)

## Notas importantes:
- ✅ El plan **Free** de Render puede ser suficiente para desarrollo/pruebas
- ⚠️ Los servidores en plan Free se duermen después de 15 minutos de inactividad
- 💡 Para producción, considera un plan pagado
- 🔐 Nunca subas claves API en el código (ahora usan variables de entorno)

## Comandos útiles para desarrollo local:
```bash
# Instalar dependencias
pip install -r gps/requirements.txt

# Ejecutar localmente
python wsgi.py

# O con gunicorn (como en Render)
gunicorn --workers 2 --bind 0.0.0.0:5000 wsgi:app
```

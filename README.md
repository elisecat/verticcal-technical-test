# Documentación del Proyecto: Verticcal Technical Test

## 1. Información General

**Nombre:** Verticcal Technical Test  
**Propósito:** Microservicio que consume datos climáticos de una API pública y expone endpoints para filtrar y procesar dicha información.  
**Tecnologías:** FastAPI, Python, y Weatherstack API.  

## 2. Estructura del Proyecto

```plaintext
📦app
 ┣ 📂application
 ┃ ┗ 📂use_cases
 ┃ ┃ ┗ 📜weather_use_case.py
 ┣ 📂domain
 ┃ ┣ 📂dto
 ┃ ┃ ┣ 📜weather_dto_request.py
 ┃ ┃ ┗ 📜weather_dto_response.py
 ┃ ┗ 📂ports
 ┃ ┃ ┗ 📜weather_port.py
 ┣ 📂infraestructure
 ┃ ┗ 📂controller
 ┃ ┃ ┗ 📜weather_controller.py
 ┣ 📂services
 ┃ ┣ 📂adapters
 ┃ ┃ ┗ 📜external_service.py
 ┗ 📜main.py
```
---

```
📦tests
 ┗ 📜test_external_service.py
``` 

---

## 3. Endpoints

### **3.1 GET `/api/external-data`**
**Descripción:** Devuelve los datos climáticos obtenidos desde Weatherstack para una ciudad específica.  
**Parámetros:**
- **`city` (query):** Nombre de la ciudad.  

**Ejemplo de Solicitud:**
```bash
curl -X GET "http://127.0.0.1:8000/api/external-data?city=Neiva"
```

**Ejemplo de Respuesta Exitosa:**
```json
{
  "success": true,
  "request": {
    "type": "City",
    "query": "Neiva, Colombia",
    "language": "en",
    "unit": "m"
  },
  "location": {
    "name": "Neiva",
    "country": "Colombia",
    "region": "Huila",
    "lat": "2.931",
    "lon": "-75.330",
    "timezone_id": "America/Bogota",
    "localtime": "2025-02-08 19:33",
    "localtime_epoch": 1739043180,
    "utc_offset": "-5.0"
  },
  "current": {
    "observation_time": "12:33 AM",
    "temperature": 29,
    "weather_code": 116,
    "weather_icons": [
      "https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png"
    ],
    "weather_descriptions": ["Partly cloudy"],
    "wind_speed": 6,
    "wind_degree": 198,
    "wind_dir": "SSW",
    "pressure": 1008,
    "precip": 0.2,
    "humidity": 55,
    "cloudcover": 25,
    "feelslike": 34,
    "uv_index": 0,
    "visibility": 10,
    "is_day": "no"
  }
}
```

---

### **3.2 POST `/api/external-data/filter`**
**Descripción:** Permite filtrar o procesar datos climáticos de una ciudad basados en un atributo específico.  
**Parámetros del Cuerpo de la Solicitud:**
- **`city` (string):** Nombre de la ciudad.
- **`attribute` (string):** Atributo a filtrar (por ejemplo, `temperature`, `humidity`).

**Ejemplo de Solicitud:**
```bash
curl -X POST "http://127.0.0.1:8000/api/external-data/filter" \
-H "Content-Type: application/json" \
-d '{
  "city": "Neiva",
  "attribute": "temperature"
}'
```

**Ejemplo de Respuesta Exitosa:**
```json
{
  "city": "Neiva",
  "attribute": "temperature",
  "value": 29
}
```

**Errores Comunes:**
- Si el atributo no existe:
```json
{
  "detail": "Atributo 'invalid_attribute' no encontrado en los datos actuales."
}
```

---

## 4. Configuración del Proyecto

### **4.1 Variables de Entorno**
Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
```ini
WEATHERSTACK_API_KEY=your_api_key_here
```

### **4.2 Instalación**
1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/verticcal-technical-test.git
   cd verticcal-technical-test
   ```

2. Crear un entorno virtual e instalar las dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt
   ```

3. Ejecutar el servidor:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## 5. Pruebas

Ejecutar pruebas unitarias:
```bash
pytest tests/
```

---

## 6. Contacto y Soporte
Para soporte técnico, por favor contacta al equipo responsable o envía un correo a **saraelissad@gmail.com**.

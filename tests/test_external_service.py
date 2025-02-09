import requests

def test_get_external_data():
    """Prueba el endpoint GET /api/external-data."""
    url = "http://127.0.0.1:8000/api/external-data?city=Neiva"
    response = requests.get(url)
    assert response.status_code == 200, f"Estado HTTP inesperado: {response.status_code}"
    data = response.json()
    assert "location" in data, "La respuesta no contiene la clave 'location'"
    assert data["location"]["name"] == "Neiva", "La ciudad no coincide con 'Neiva'"
    print("✅ Prueba exitosa: GET /api/external-data")

def test_post_external_data_filter():
    """Prueba el endpoint POST /api/external-data/filter."""
    url = "http://127.0.0.1:8000/api/external-data/filter"
    payload = {
        "city": "Neiva",
        "attribute": "temperature"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 200, f"Estado HTTP inesperado: {response.status_code}"
    data = response.json()
    assert data["city"] == "Neiva", "La ciudad no coincide con 'Neiva'"
    assert data["attribute"] == "temperature", "El atributo no coincide con 'temperature'"
    assert "value" in data, "La respuesta no contiene la clave 'value'"
    print("✅ Prueba exitosa: POST /api/external-data/filter")

if __name__ == "__main__":
    test_get_external_data()
    test_post_external_data_filter()
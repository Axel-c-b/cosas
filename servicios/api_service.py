import requests
from auxiliares.api_data import API_URL

class APIService:
    @staticmethod
    def obtener_datos(endpoint):
        response = requests.get(f"{API_URL}/{endpoint}")
        return response.json() if response.status_code == 200 else []

    @staticmethod
    def crear_dato(endpoint, datos):
        response = requests.post(f"{API_URL}/{endpoint}", json=datos)
        return response.status_code == 201

    @staticmethod
    def actualizar_dato(endpoint, id_dato, datos):
        response = requests.put(f"{API_URL}/{endpoint}/{id_dato}", json=datos)
        return response.status_code == 200

    @staticmethod
    def eliminar_dato(endpoint, id_dato):
        response = requests.delete(f"{API_URL}/{endpoint}/{id_dato}")
        return response.status_code == 200
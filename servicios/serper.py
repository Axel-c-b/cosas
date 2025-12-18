import requests
import json

def busqueda():
    url = "https://google.serper.dev/search"
    valor=input('Qué desea buscar?...')

    payload = json.dumps({
    "q": valor
    })
    headers = {
    'X-API-KEY': '68020f011b6756a004d4aaf937b8a12ad58adad1',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
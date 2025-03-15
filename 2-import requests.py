import requests

params = {
    "idFuelType": "ALL",
    "fechaInicio": "2025-02-25",
    "fechaFin": "2025-02-26"
}

url = "https://api.precioil.es/precioMedioDiario"

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Daily Average Fuel Prices:")
    print(data)
else:
    print(f"Error in request: {response.status_code}")
    print(response.json())

fuel_types = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for fuel_id in fuel_types:
    params = {
        "idFuelType": str(fuel_id),
        "fechaInicio": "2025-02-25",
        "fechaFin": "2025-02-26"
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data:
            print(f"Fuel ID {fuel_id}: {data}")
    else:
        print(f"Fuel ID {fuel_id} - Error: {response.status_code}")

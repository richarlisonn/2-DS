import requests

response = requests.get(https://servicodados.ibge.gov.br/api/v1/localidades/distritos)

print(response.status.code)
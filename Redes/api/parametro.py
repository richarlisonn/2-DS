import requests

url = ('https://servicodados.ibge.gov.br/api/v1/localidades/distritos/291790410')

response = requests.get(url)
distritos= response.json()
print(distritos)
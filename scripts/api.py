import requests
import json

def cep_select(cep):
    url = ('https://viacep.com.br/ws/{}/json/'.format(cep))
    req = requests.get(url, timeout = 3000)
    cep_return = req.json()
    print(cep_return)
    return cep_return

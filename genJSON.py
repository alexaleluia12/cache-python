import json

from faker import Faker

fake = Faker()
start = 60
base = {"nome": "","endereco":"","descricao":"","outros":"","id":1}

max_ = 1000000
nome = ""
endereco = ""
descricao = ""
outros = ""


while True:
    nome += fake.text()
    endereco += fake.text()
    descricao += fake.text()
    outros += fake.text()

    sum_lenth = len(nome) + len(endereco) + len(descricao) + len(outros)
    if sum_lenth >= max_ - start:
        break

base['nome'] = nome
base['endereco'] = endereco
base['descricao'] = descricao
base['outros'] = outros

with open('ref.json', 'w') as f:
    json.dump(base, f)

print('nd')


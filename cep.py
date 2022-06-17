import requests
from tqdm import tqdm
import os

# passo 1: pegar a lista de ceps
with open("ceps.txt", "r") as arquivo:
    ceps = arquivo.read()
ceps = ceps.split("\n")

# passo 2: pegar as informações de cada cep
enderecos = []
for cep in tqdm(ceps):
    link = f"https://cep.awesomeapi.com.br/json/{cep}"
# passo 3: verificar se a cidade é João Pessoa
    requisicao = requests.get(link)
    resposta = requisicao.json()
    cidade = resposta['city']
    bairro = resposta['district']
    rua = resposta['address']
# passo 4: printar o cep e o bairro
    if cidade == "João Pessoa":
        enderecos.append((cep, rua, bairro))
os.system("cls")
for i in enderecos:
    print(i)


    

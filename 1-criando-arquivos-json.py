import json

with open('0-dados-json.txt', 'r') as texto:
    arquivo = texto.readlines()
arquivo_json = []
for indice, linha in enumerate(arquivo):
    if '###' in linha and '**' in linha:
        print('entrei em outro json')
        indice_inicio = indice + 2
        nome_arquivo = f'{linha[10:-3]}.json'
        
    
    if indice_inicio <= indice:
        arquivo_json.append(linha)
    
    if linha == '```\n':
        arquivo_json.pop(-1)
        with open(nome_arquivo, 'w') as novo_arquivo:
            novo_arquivo.writelines(arquivo_json)
        arquivo_json = []

    


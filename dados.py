#manipulação do arquivo .json 
import json

def ler(caminho_arquivo):
    try:
        #abre o arquivo em modo leitura
        with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
            return json.load(arquivo) # converte o texto do arquivo JSON de volta para uma lista de dicionários
    except FileNotFoundError:
        return [] # Se não achar o arquivo, devolve uma lista vazia
        
    

def salvar(lista, caminho_arquivo):
    # Abre o arquivo no modo escrita ('w' de write). 
    # O 'w' apaga tudo que tinha antes e escreve por cima. Se o arquivo não existir, ele cria um novo.
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista,arquivo,indent=2, ensure_ascii=False) # Pega a sua lista do Python e converte em texto JSON

# PROJETO: FINANCEIRO PRO (JSON EDITION)
"""
Criar um programa de terminal que gerencie seus gastos diários. Ao contrário da lista de tarefas, onde cada item era apenas uma frase, aqui cada "gasto" é um objeto composto por um nome e um valor. Os dados devem persistir em um arquivo chamado gastos.json.
# Uma lista que contém dicionários
gastos = [
    {"item": "Internet", "valor": 120.50},
    {"item": "Mercado", "valor": 450.32}
]

Funcionalidades Esperadas
Adicionar Gasto:

O programa deve pedir o nome do item.

O programa deve pedir o valor (certifique-se de converter para float).

O novo gasto deve ser salvo imediatamente no JSON.

Listar Gastos:

Exibir de forma organizada todos os gastos salvos.

Comando total:

O programa deve percorrer a lista, somar todos os valores e exibir o total acumulado.

Limpeza (clear) e Saída (sair):

Manter a organização do terminal e a saída segura.
"""
import json
import sys

def listar(gastos):
    print()
    if not gastos:
        print('Nenhum gasto para listar')
        return
    print('Gastos:')
    for gasto in gastos:
        print(f"\t{gasto['gasto']} ({gasto['vencimento']}): {gasto['valor']}")
    print()

def adicionar(gastos):
    print()
    while True:
        nome_gasto = input('Nome do gasto: ').strip().lower()
        if nome_gasto: # Se tiver algo digitado, quebra o loop
            break
        print('Você não digitou o nome do gasto')
    
    while True:
        data_vencimento = input('Digite a data de vencimento: ').strip().lower()
        if data_vencimento:
            break
        print('Você não digitou a data de vencimento')

    while True:
        valor = input('Valor do gasto: ').strip().replace(',','.')
        try:
            valor_gasto = float(valor)
            break
        except ValueError:
            print('Valor inválido! Digite apenas números')
    print(f'Gasto adicionado com sucesso!')
    novo_gasto = {'gasto':nome_gasto, 'vencimento': data_vencimento,'valor': valor_gasto}
    gastos.append(novo_gasto)
    print()

def total(gastos):
    print()
    total = 0
    for item in gastos:
        total += item['valor']
    print(f'Gasto total: R${total:.2f}')

def retirar_gasto(gastos):
    print()
    gasto_retirar = input('Qual gasto retirar? ').strip().lower()
    indice_gasto = None

    for i, item in enumerate(gastos):
        if item['gasto'] == gasto_retirar:
            indice_gasto = i
            break

    if indice_gasto is not None:
        gastos.pop(indice_gasto)
        print('Gasto removido!')
    else:
        print('Gasto não encontrado')

def ler(caminho_arquivo):
    try:
        with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return [] # Se não achar o arquivo, devolve uma lista vazia
        
    

def salvar(lista, caminho_arquivo):
    # Abre o arquivo no modo escrita ('w' de write). 
    # ATENÇÃO: O 'w' apaga tudo que tinha antes e escreve por cima. Se o arquivo não existir, ele cria um novo.
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista,arquivo,indent=2, ensure_ascii=False) # Pega a sua lista do Python e converte em texto JSON
 
CAMINHO_ARQUIVO = 'gastos2.json'
gastos = ler(CAMINHO_ARQUIVO)

while True:
    print('Comandos: adicionar, retirar, listar, total, sair')
    tarefa = input('Digite um comando: ').lower().strip()

        
    comandos = { #Para impedir que o Python execute a função na hora errada, nós precisamos "embrulhar" ela em um pacote. É isso que o lambda faz.
            'adicionar': lambda: adicionar(gastos), #(lambda:). O único trabalho dessa mini-função é guardar a instrução adicionar(gastos) dentro dela. Guarde essa mini-função no dicionário, mas NÃO A EXECUTE AINDA.
            'listar': lambda: listar(gastos),
            'total': lambda: total(gastos),
            'retirar': lambda: retirar_gasto(gastos),
            'sair': lambda: sys.exit(0),
        }

    if tarefa in comandos: # 1. Checa se o que o usuário digitou (ex: 'adicionar') existe no seu dicionário
        # 2. Vai no dicionário e pega o VALOR guardado naquela chave. 
        # Lembra que o valor é um 'lambda'? Lambda é só um apelido para "uma função guardada".
        # Então, a variável 'comando' agora é uma função esperando para ser ativada!
        comando = comandos.get(tarefa)
        comando() # 3. Os parênteses () são o gatilho! Eles dizem: "Execute a função que pegamos agora mesmo!"
        # A função acima acabou de rodar. Talvez ela tenha adicionado um item, 
        # talvez tenha removido. A lista 'gastos' mudou! 
        # Para não perder o dado se acabar a energia do PC, nós salvamos a lista nova no JSON IMEDIATAMENTE.
        salvar(gastos,CAMINHO_ARQUIVO)
    else:
        print('Digite um comando disponível\n')

        
        
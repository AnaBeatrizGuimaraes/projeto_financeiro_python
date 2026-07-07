#Ficará com as funções matemáticas puras e a importação de datas.
import os
from datetime import datetime
import rich
from rich.table import Table
from rich.console import Console


CATEGORIAS_VALIDAS = ['alimentacao', 'transporte', 'lazer', 'saude', 'educacao', 'outros']


console = Console()


def listar(gastos):
    print()
    if not gastos: # verifica se a lista está vazia
        print('Nenhum gasto para listar')
        return #encerra a função se não houver gastos
    
    tabela = Table(title = "Minhas Finanças")

    tabela.add_column("ID", justify= "center", style= "blue")
    tabela.add_column("Gasto", justify= "center", style= "magenta")
    tabela.add_column("Categoria", justify= "center", style= "green")
    tabela.add_column("Data", justify= "center", style= "red")
    tabela.add_column("Valor", justify= "left", style= "yellow")
    

    for i, gasto in enumerate(gastos): #percorre cada dicionário dentro da lista
        tabela.add_row(str(i), gasto['gasto'], gasto['categoria'], gasto['data'], f"R$ {gasto['valor']:.2f}")

    console.print(tabela)
def adicionar(gastos):
    print()
    while True: #validação da categoria 
        print(f"Categorias disponíveis: {', '.join(CATEGORIAS_VALIDAS)}")
        nome_categoria = input('Digite a categoria do gasto: ').strip().lower()
        if nome_categoria in CATEGORIAS_VALIDAS:
            break
        print(f'Categoria inválida! Escolha uma destas: {", ".join(CATEGORIAS_VALIDAS)}')


    while True: # validação do nome
        nome_gasto = input('Nome do gasto: ').strip().lower()
        if nome_gasto: # Se tiver algo digitado, quebra o loop
            break
        print('Você não digitou o nome do gasto')
    
    while True: # validação da data
        data_compra= input('Digite a data de compra: ').strip().lower()
        try:
            datetime.strptime(data_compra, "%d/%m/%Y") # tenta converter o texto na data no formato %d/%m/%Y
            break 
        except ValueError: # se a conversão falhar( letras ou uma data impossível)
            print("Digite a data no formato dd/mm/aaaa")

    while True: # validação do valor
        valor = input('Valor do gasto: ').strip().replace(',','.') # troca vírgula por ponto para não quebrar o float
        try:
            valor_gasto = float(valor) # tenta converter texto em número decimal
            break
        except ValueError: # se digitar letras, lança o erro
            print('Valor inválido! Digite apenas números')
    print(f'Gasto adicionado com sucesso!')
    # cria um novo dicionário com as variáveis capturadas
    novo_gasto = {'gasto':nome_gasto, 'categoria':nome_categoria, 'data': data_compra,'valor': valor_gasto}
    # adiciona esse dicionário ao final da lista existente
    gastos.append(novo_gasto)
    print()

def edita_gasto(gastos):
    indice_editar = input("Digite o ID do gasto que deseja editar: ")

    print()

    try:
        int_indice = int(indice_editar)
        gasto_editar = gastos[int_indice]
        while True:
            novo_valor = input("Digite o novo valor: ").strip().replace(',','.')
            try:
                novo_valor_float = float(novo_valor) # tenta converter texto em número decimal
                break
            except ValueError: # se digitar letras, lança o erro
                print('Valor inválido! Digite apenas números')

        gasto_editar['valor'] = novo_valor_float
        
        
        print("Gasto editado com sucesso!")
    except IndexError:
        print("Esse ID não existe!")

    except ValueError:
        print("Por favor, digite apenas números inteiros!")
def total(gastos):
    print()
    total = 0
    for item in gastos:
        total += item['valor'] #soma o valor de cada dicionário ao total
    console.print(f"[bold green]Gasto total acumulado: R$ {total:.2f}[/bold green]")

def total_por_categoria(gastos):
    print()
    subtotal = {} # acumulador vazio

    for gasto in gastos:
        categoria_atual = gasto['categoria']
        valor_atual = gasto['valor']

        if categoria_atual in subtotal:
            subtotal[categoria_atual] += valor_atual
        else:
            subtotal[categoria_atual] = valor_atual
    
    return subtotal

def exibir_total_categoria(gastos):
    
    dados_calculados = total_por_categoria(gastos)

    tabela = Table(title = "Total por Categoria")
    tabela.add_column("Categoria", justify= "center", style= "blue")
    tabela.add_column("Subtotal", justify= "center", style= "red")

    for categoria, valor in dados_calculados.items():
        tabela.add_row(categoria.capitalize(), f"R$ {valor:.2f}")

    console.print(tabela)

def filtrar_por_categoria(gastos):
    categoria_escolhida = input("Digite a categoria que deseja buscar: ").strip().lower()

    gastos_categoria = []

    for gasto in gastos:
        if gasto['categoria'] == categoria_escolhida:
            gastos_categoria.append(gasto)
    
    if not gastos_categoria:
        print("Nenhum gasto foi encontrado!")

    tabela = Table(title = f"{categoria_escolhida}")

    tabela.add_column("Gasto", justify= "center", style= "blue")
    tabela.add_column("Data", justify= "center", style= "magenta")
    tabela.add_column("valor", justify= "left", style= "green")


    for i, gasto in enumerate(gastos_categoria): #percorre cada dicionário dentro da lista
        tabela.add_row(gasto['gasto'], gasto['data'], f"R$ {gasto['valor']:.2f}")

    console.print(tabela)


def retirar_gasto(gastos):
    print()
    numero = input("Digite o ID: ")
    try:
        gastos.pop(int(numero))
        print("ID removido!")
    except ValueError:
        print("Por favor, digite apenas números inteiros!")
    except IndexError:
        print("Esse ID não existe na lista!")


def limpar_tela(): # função para limpar a tela = sempre que o loop reiniciar, terminal ficará limpo
    if os.name == 'nt': # se for windows
        os.system('cls')
    else:
        os.system('clear')


def relatorio_mensal(gastos):
    while True: # validação da data
        data_relatorio= input('Digite a data desejada para gerar o relatório (MM/AAAA): ').strip().lower()
        try:
            datetime.strptime(data_relatorio, "%m/%Y") # tenta converter o texto na data no formato %m/%Y
            break 
        except ValueError: # se a conversão falhar( letras ou uma data impossível)
            print("Digite a data no formato MM/AAAA")
    
    gastos_filtrados = [] #lista para adicionar gastos que sejam do mes digitado pelo usuario

    for gasto in gastos:
        if data_relatorio == gasto['data'][3:]: # se a data do gasto for a mesma que o usuario digitou -> adiciona na lista
            gastos_filtrados.append(gasto)

    if not gastos_filtrados:
        print("Não há gastos registrados nesse mês!")
        return None
        

    total_mes = 0

    for gasto in gastos_filtrados:
        total_mes += gasto['valor']
    
    #crio uma lista ordenada do maior para o menor valor
    gastos_ordenados = sorted(gastos_filtrados, key = lambda gasto: gasto['valor'], reverse= True)

    maior_gasto_mes = gastos_ordenados[0]

    subtotais_mes = total_por_categoria(gastos_filtrados)

    pacote_dados = {
        'total_calculado': total_mes,
        'extrato_ordenado': gastos_ordenados,
        'resumo_categorias': subtotais_mes
    }

    return pacote_dados

def exibir_relatorio_mensal(pacote_dados):
    if pacote_dados is None:
        return 
    total_exibir = pacote_dados['total_calculado']
    lista_ordenada = pacote_dados['extrato_ordenado']
    categorias_exibir = pacote_dados['resumo_categorias']

    tabela = Table(title = "Relatório Mensal")

    console.print(f"[bold green]Gasto total no mês: R$ {total_exibir:.2f}[/bold green]")

    item_mais_caro = lista_ordenada[0]
    nome_item_mais_caro = item_mais_caro['gasto']
    valor_item_mais_caro = item_mais_caro['valor']

    console.print(f"[bold red]Maior gasto do mês: {nome_item_mais_caro} -> R$ {valor_item_mais_caro:.2f}[/bold red]")
    tabela.add_column("Categoria", justify= "center", style= "blue")
    tabela.add_column("Subtotal", justify= "center", style= "red")

    for categoria, valor in categorias_exibir.items():
        tabela.add_row(categoria.capitalize(), f"R$ {valor:.2f}")

    console.print(tabela)


        
        
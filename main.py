import dados
import operacoes

CAMINHO_ARQUIVO = 'gastos2.json' #nome do arquivo para guardar os dados
gastos = dados.ler(CAMINHO_ARQUIVO) # lê o arquivo JSON e converte para uma lista de dicionários

comandos = { #Para impedir que o Python execute a função na hora errada, nós precisamos "embrulhar" ela em um pacote. É isso que o lambda faz.
            '1': lambda: operacoes.adicionar(gastos), 
            '2': lambda: operacoes.retirar_gasto(gastos),
            '3': lambda: operacoes.edita_gasto(gastos),
            '4': lambda: operacoes.listar(gastos),
            '5': lambda : operacoes.exibir_total_categoria(gastos),
            '6': lambda: operacoes.total(gastos),
            '7': lambda: operacoes.exibir_relatorio_mensal(operacoes.relatorio_mensal(gastos)),
            '8': lambda: operacoes.filtrar_por_categoria(gastos)
        }

while True:
    menu = """
Escolha uma opção:
1) Adicionar
2) Retirar
3) Editar
4) Listar
5) Total por categoria
6) Total
7) Relatório mensal
8) Filtrar por categoria
9) Sair
"""
    print(menu)
    tarefa = input('Digite uma das opções: ').lower().strip()

    if tarefa == '9':
        print("Saindo do programa...")
        break

    operacoes.limpar_tela()

    if tarefa in comandos: 
        comando = comandos.get(tarefa)
        comando() 
     
        dados.salvar(gastos,CAMINHO_ARQUIVO)
    else:
        print('Digite uma opção disponível\n')

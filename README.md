# 💰 Gerenciador Financeiro (CLI)

Um sistema de gerenciamento financeiro pessoal via terminal, desenvolvido em Python. Este projeto aplica conceitos sólidos de modularização de código, persistência de dados em arquivos locais e formatação visual avançada para uma melhor experiência do usuário.

---

## 🚀 Funcionalidades

* **Adicionar Despesas:** Permite registrar novos gastos validando rigorosamente informações de nome, data, valor e categorias pré-definidas (alimentação, transporte, lazer, saúde, educação e outros).
* **Listagem Visual:** Exibe todos os registros financeiros formatados em uma tabela interativa.
* **Edição de Dados:** Capacidade de buscar um ID específico e alterar o seu valor financeiro de forma dinâmica.
* **Remoção de Registros:** Permite excluir permanentemente um gasto da base de dados fornecendo o seu ID correspondente.
* **Filtros por Categoria:** Busca iterativa que varre os registros e exibe apenas as despesas correspondentes a uma categoria escolhida pelo usuário.
* **Totalizadores:** Calcula matematicamente o gasto total acumulado e gera uma tabela com o subtotal dividido por categoria.
* **Resumo Mensal:** Gera um relatório de um mês e ano específicos, destacando o gasto total do período, os subtotais categorizados e identificando o maior gasto (vilão do mês).
* **Persistência de Dados:** Salva automaticamente todas as inserções, edições e exclusões em um arquivo local `.json` para manter o estado da aplicação salvo entre as sessões.

---

## 🛠️ Tecnologias e Bibliotecas

* **Python:** Linguagem base da aplicação.
* **JSON:** Biblioteca nativa utilizada para a conversão de listas de dicionários em formato de texto para armazenamento.
* **Datetime:** Biblioteca nativa utilizada para realizar o *parsing* e a validação estrita das datas no formato `DD/MM/AAAA` e `MM/AAAA`.
* **Rich:** Biblioteca externa responsável pela criação da interface gráfica baseada em texto (TUI), renderizando tabelas estruturadas e textos estilizados com cores no terminal.
* **OS:** Biblioteca nativa utilizada para limpar a tela do terminal (compatível com Windows e sistemas Unix) a cada nova iteração do menu principal.

---

## 📁 Estrutura do Projeto (Arquitetura)

O código adota uma separação pragmática de responsabilidades, dividindo o escopo em três módulos fundamentais:

| Arquivo | Responsabilidade |
| :--- | :--- |
| `main.py` | Atua como o roteador principal do sistema. Exibe o menu numérico de opções (1 a 9), captura a entrada do usuário e aciona a função correspondente usando um dicionário de funções *lambda*, além de invocar o salvamento dos dados ao fim de cada operação. |
| `operacoes.py` | O motor do sistema. Contém toda a lógica de negócio, cálculos matemáticos, validação de exceções (`try/except`) e a renderização das tabelas visuais usando o *Rich*. |
| `dados.py` | Módulo de persistência isolado. Contém exclusivamente as funções `ler()` e `salvar()` responsáveis por abrir e manipular o arquivo de texto. |
| `gastos2.json` | Arquivo de banco de dados gerado de forma autônoma pelo sistema para armazenar os registros localmente. |

---

## 💻 Como Executar na sua Máquina

1. Certifique-se de ter o **Python 3** instalado.
2. Instale a biblioteca visual executando o seguinte comando no seu terminal:
   ```bash
   pip install rich

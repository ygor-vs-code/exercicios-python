funcionarios = [
    {'nome': 'Ana', 'idade': 28, 'salario': 3200},
    {'nome': 'Bruno', 'idade': 35, 'salario': 4100},
    {'nome': 'Clara', 'idade': 40, 'salario': 5100},
]

def lista_funcionarios(dicionario):
    selecionados = [
        {**funcionario, 'salario': funcionario['salario'] * 1.10}
        for funcionario in dicionario
        if funcionario['idade'] > 30
    ]
    
    nova_lista = {
        funcionario['nome']: funcionario['salario']
        for funcionario in selecionados
    }
    
    print(nova_lista)

lista_funcionarios(funcionarios)
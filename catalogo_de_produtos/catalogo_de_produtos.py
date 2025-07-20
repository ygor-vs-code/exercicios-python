produtos = [
    {'nome': 'Feijão', 'preco': 12.5, 'quantidade': 3}
]

def adicionar_produto(lista, nome, preco, quantidade):
    nomes = set ()
    for item in lista:
        nomes.add(item['nome'])

    if nome not in nomes:
        produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade}
        lista.append(produto)
        print(f'\nProduto "{nome}" adicionado com sucesso!\n')
    else:
        print('\nERRO! Esse produto já existe.\n')


def buscar_preco(lista, nome):
    for produto in lista:
        if produto['nome'].lower() == nome.lower():
            return f'\nO preço de "{nome}" é R$ {produto["preco"]:.2f}\n'

    print(f'\nProduto "{nome}" não encontrado.\n')


def atualizar_estoque(lista, nome, nova_qtd):
    for produto in lista:
        if produto['nome'].lower() == nome.lower():
            produto['quantidade'] = nova_qtd
            return f'\nProduto "{nome}" atualizado. Nova quantidade: {produto["quantidade"]}\n'
        
def resumo_produtos(lista):
    print()
    for item in lista:
        total = item['preco'] * item['quantidade']
        print(f'Nome: {item["nome"]} '
              f'| Preço: R$ {item["preco"]:.2f} '
              f'| Quantidade: {item["quantidade"]} '
              f'| Total: R$ {total:.2f}'
              ) 
    print()


def main():
    while True:
        print('1. Adicionar\n' \
        '2. Buscar Preço\n' \
        '3. Atualizar Estoque\n' \
        '4. Resumo dos Produtos\n' \
        '5. Sair\n')

        entrada = input('\nDigite uma opção: ')

        if entrada == '5':
            print('Programa Encerrado.')
            break
            
        elif entrada == '1':
            try:
                print('\nDigite os seguintes dados para adicionar o produto:\n')
                nome = input('Nome do produto: ')
                preco = float(input('Preço unitário do produto: '))
                quantidade = int(input('Quantidade do produto: '))
                adicionar_produto(produtos, nome, preco, quantidade)
            except ValueError:
                print('Valor Inválido!')
        
        elif entrada == '2':
            nome = input('\nDigite o nome do produto: ')
            resultado = buscar_preco(produtos, nome)

            if resultado == None:
                print(f'Produto "{nome}" não encontrado')
            else:
                print(resultado)

        elif entrada == '3':
            try:
                nome = input('\nDigite o nome: ')
                nova_qtd = int(input('Digite nova quantidade: '))
                resultado = atualizar_estoque(produtos, nome, nova_qtd)
                if resultado == None:
                    print('Produto não encontrado')
                else:
                    print(resultado)
            except ValueError:
                print('Valor Inválido')

        elif entrada == '4':
            resumo_produtos(produtos)
        
        else:
            print(f'Opção "{entrada}" inválida!')

main()
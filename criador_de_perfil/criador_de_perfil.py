nome = input('Nome: ')
idade = input('Idade: ')
cidade = input('Cidade: ')
profissao = input('Profissão: ')
perfil = {
    'nome': nome,
    'idade': idade,
    'cidade': cidade,
    'profissao': profissao,
}

def criar_perfil(**kwargs):
    print('\nPerfil criado com os seguintes dados:')
    for chave, valor in kwargs.items():
        print(f'- {chave.capitalize()}: {valor}')
    
criar_perfil(**perfil)
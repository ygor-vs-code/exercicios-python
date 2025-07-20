import random

def criar_player():
    nome = input('Digite seu nome: ')
    return {
        "nome": nome,
        "vida": 140,
        "pocoes": 4,
        "vida_maxima": 140,
        "esquivando": False,
        "bloqueando": False
    }

def criar_boss():
    return {
        "nome": 'Pescotapa Dev Assembly',
        "vida": 750,
        "vida_maxima": 750,
        "bloqueando": False
    }

def mostrar_status(jogador, boss):
    print('=' * 40)
    print(f'{jogador["nome"]} - Vida: {jogador["vida"]} | Poções: {jogador["pocoes"]}')
    print(f'{boss["nome"]} - Vida: {boss["vida"]}')
    print('=' * 40)

def vez_jogador(jogador, boss):
    print('Digite uma ação:')
    print('1 - Atacar')
    print('2 - Usar poção')
    print('3 - Esquivar')
    print('4 - Bloquear')
    acao = input('Escolha (1, 2, 3 ou 4): ')

    if acao == '1':
        dano, critico = calcular_dano(50, 70)
        boss['vida'] -= dano
        if critico:
            print(f'\nAtaque CRÍTICO! Você causou {dano} de dano ao {boss["nome"]}!')
        else:
            print(f'\nVocê causou {dano} de dano ao {boss["nome"]}!')
        jogador["esquivando"] = False
        jogador["bloqueando"] = False
    elif acao == '2':
        usar_pocao(jogador)
        jogador["esquivando"] = False
        jogador["bloqueando"] = False
    elif acao == '3':
        jogador["esquivando"] = True
        jogador["bloqueando"] = False
        print('\nVocê se preparou para esquivar do próximo ataque!')
    elif acao == '4':
        jogador["bloqueando"] = True
        jogador["esquivando"] = False
        print('\nVocê está bloqueando o próximo ataque para reduzir dano pela metade!')
    else:
        print('\nAção inválida. Você perdeu a vez.')
        jogador["esquivando"] = False
        jogador["bloqueando"] = False

def usar_pocao(jogador):
    if jogador["pocoes"] > 0:
        cura = random.randint(70, 90)
        jogador["vida"] += cura
        if jogador["vida"] > jogador["vida_maxima"]:
            jogador["vida"] = jogador["vida_maxima"]
        jogador["pocoes"] -= 1
        print(f'\nVocê usou uma poção e recuperou {cura} de vida.')
    else:
        print('\nVocê não tem mais poções!')

def vez_boss(jogador, boss):
    print(f'\n{boss["nome"]} vai atacar!')

    dano, critico = calcular_dano(20, 30)
    mensagem_extra = ''

    if jogador["esquivando"]:
        if random.random() < 0.5:
            print('Você esquivou com sucesso e não sofreu dano!')
            dano = 0
        else:
            mensagem_extra = " (esquiva falhou🤣)"
    elif jogador["bloqueando"]:
        dano = dano // 2
        mensagem_extra = " (dano reduzido pelo bloqueio)"

    jogador["vida"] -= dano

    if dano > 0:
        if critico:
            print(f'{boss["nome"]} causou {dano} de DANO CRÍTICO em você!{mensagem_extra}')
        else:
            print(f'{boss["nome"]} causou {dano} de dano em você!{mensagem_extra}')

    jogador["esquivando"] = False
    jogador["bloqueando"] = False


def calcular_dano(min_dano, max_dano):
    dano = random.randint(min_dano, max_dano)
    critico = random.random() < 0.2
    if critico:
        dano *= 2
    return dano, critico

def verificar_fim(jogador, boss):
    if boss["vida"] <= 0:
        print(f'\nVocê derrotou o {boss["nome"]}! Vitória!\n')
        return True
    elif jogador["vida"] <= 0:
        print(f'\nVocê foi derrotado pelo {boss["nome"]}... Fim de jogo, ruim.\n')
        return True
    return False

def jogar():
    jogador = criar_player()
    boss = criar_boss()

    print(f'\n{jogador["nome"]}, você vai enfrentar o {boss["nome"]}!\n')

    while True:
        mostrar_status(jogador, boss)
        vez_jogador(jogador, boss)

        if verificar_fim(jogador, boss):
            break

        vez_boss(jogador, boss)

        if verificar_fim(jogador, boss):
            break

jogar()


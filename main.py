import random

print('Gerador de senhas!')

alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./!@#$?'

quantas_senhas = int(input('Você deseja gerar quantas senhas?: '))
tamanho_senha = int(input('Qual tamanho que deseja para sua senha?: '))

print('Senha(s) gerada(s)!', end='\n')

for senha in range(quantas_senhas):
    senhas = ''
    for i in range(tamanho_senha):
        senhas += random.choice(alfabeto)
    print(senhas)
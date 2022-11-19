from datetime import datetime


dados = dict()


# perguntas para o dados
dados['Nome: '] = str(input('Nome: '))
while True:    
    dados['Sexo: ']=str(input('sexo[M/F]')).strip().upper()[0]
    if dados['Sexo: '] in'MF':
        break
    print('Erro sexo invalido!')
nac = int(input('Ano de nascimento: '))
dados['Idade: '] = datetime.now().year - nac
dados['ctps: '] = int(input('Carteira de Trabalho(Pis,caso não houver digite 0): '))

# Area de calculo do ctps/inss
if dados['ctps: '] != 0:
    dados['Contratação: '] = int(input('Ano de contratação: '))
    dados['Salário: R$'] = float(input('Salário: R$'))
    if dados['Salário: R$'] <= 1212.00:
        Desconto = dados['Salário: R$']*0.075
    elif dados['Salário: R$'] >= 1212.00 and dados['Salário: R$']<=2427.35:
        Desconto = dados['Salário: R$']*0.09
    elif dados['Salário: R$'] >= 2427.36 and dados['Salário: R$']<= 3641.03:
        Desconto = dados['Salário: R$']
    elif dados['Salário: R$'] >= 3641.03:
        Desconto = dados['Salário: R$']*0.14
    dados['Desconto do Inss: R$'] = Desconto
    if dados['Sexo: ']=='M':
        dados['Aposentadoria com a idade: '] = dados['Idade: '] + ((dados['Contratação: '] + 35)-datetime.now().year)
    else:
        dados['Aposentadoria com a idade: '] = dados['Idade: '] + ((dados['Contratação: '] + 30)-datetime.now().year)
print('-='*30)

# print na tela
for n, v in dados.items():
    print(f' -> {n}{v}')

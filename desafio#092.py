from datetime import datetime
dados=dict()
dados['Nome: ']=str(input('Nome: '))
nac=int(input('Ano de nascimento: '))
dados['Idade: ']=datetime.now().year - nac
dados['ctps: '] = int(input('Carteira de Trabalho (o valor 0 é porque não tem ctps): '))
if dados['ctps: '] !=0:
    dados['Contratação: '] = int(input('Ano de contratação: '))
    dados['Salário: ']=float(input('Salário: R$'))
    dados['Aposentadoria com a idade: '] = dados['Idade: ']+((dados['Contratação: '] +35)-datetime.now().year)
print('-='*30)
for n,v in dados.items():
    print(f' -> {n}{v}')

from time import sleep
def contador(a,b,c):
    for v in range(a,b,c):
        print(v,end='|')
    print()
        


contador(1,11,1)
contador(-10,0,2)
ini=int(input('Inicio -> '))
fim=int(input('Fim -> '))
pas=int(input('Pulador -> '))
contador(ini,fim+1,pas)
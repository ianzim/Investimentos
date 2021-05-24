from FileHandeling import *
import os
class Carteira:
    def __init__(self, aplicado=0, rendimento_mes=0, montante=0 ):
        self.aplicado = aplicado
        self.rendimento_mes = rendimento_mes
        self.montante  = montante

    def total(self):
        return self.montante

    def get_inicial(self):
        return self.aplicado

def cabec(txt):
    print()
    print('-'*51)
    print(f'{txt:^51}')
    print('-'*51)
    print()

def get_mes():
    meses = ('Jan', 'Fev', 'Mar', 'Abril', 'Maio', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez')
    mes_aplicação = int(input("Qual o mês da aplicação? (ex: Janeiro: Digite '1') ")) - 1
    mes_inicial = meses[mes_aplicação]
    t = int(input(f"Quantos meses durará a aplicação? "))
    
    if mes_aplicação + t > len(meses) - 1:
        mes_final = meses[(mes_aplicação + t) - 12*((mes_aplicação + t)//12)]

    else:
        mes_final = meses[mes_aplicação + t]

    return [mes_inicial, mes_final, t]

def novoInvestimento():
    mes = get_mes()
    c = float(input("Dinheiro inicial aplicado: R$ "))
    c_inicial = c
    i = (float(input("Taxa de juros (em %): "))) / 100
    aplic_secund = float(input("Valor a ser adicionado ao investimento por mês: R$ "))
    m = 0

    for tempo in range(mes[2]):
        if tempo == 0:
            m = c * (1+i)
        else:
            c = m + aplic_secund
            m = c * (1+i)

    c = c_inicial

    carteira = Carteira(c, i, m)

    inicial = carteira.get_inicial()
    montante = carteira.total()

    print(f'Com a aplicação de {inicial} por {mes[2]} meses, você terá {montante:.2f} ao final do processo')

    try:
        file = open('Carteira.txt', 'a')
    except FileNotFoundError:
        file = create_file('Carteira.txt', 'wt+')
    else:
        file.write(f'{mes[0]}-{mes[1]}->R${inicial:.2f};R${montante:.2f};{mes[2]} meses\n')
    finally:
        file.close()

def verInvestimentos():
    try:
        read_file('Carteira.txt')
    except FileNotFoundError:
        print("VOCÊ NÃO FEZ INVESTIMENTOS. REALIZE ALGUM PARA PODER VIZUALIZAR ESTA FUNÇÃO")

def main():
    while True:
        cabec('SELECIONE SUA OPÇÃO')
        opc = ['Realizar um novo investimento', 'Ver investimentos passados']
        for i, v in enumerate(opc):
            print(f'[{i+1}]..... {v}')
        op = int(input("Digite sua opção: "))
        if op == 1:
            cabec("REALIZE UM INVESTIMENTO")
            novoInvestimento()
        elif op == 2:
            cabec('SEUS INVESTIMENTOS')
            verInvestimentos()
        
        continuar = str(input("Quer continuar? [S/N] ").upper())
        if continuar != "S" and continuar != "N":
            while continuar != "S" and continuar != "N":
                continuar = str(input("Quer continuar? [S/N] ").upper())
                if continuar == 'N':
                    break
        if continuar == 'N':
            break

        elif continuar == 'S':
            os.system('cls' if os.name == 'nt' else 'clear')
        
main()
input('Pressione "ENTER" para sair')

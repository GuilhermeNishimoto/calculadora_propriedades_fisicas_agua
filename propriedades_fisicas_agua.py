# Calculadora Propriedades Físicas da Água 

# Importando as bibliotecas
from math import e
import pandas as pd

def densidade(temperatura):
    # Retorna o valor da densidade da água em kg/m³
    return -0.000000125767*(temperatura**4)+0.000177892106*(temperatura**3)-0.096908373061*(temperatura**2)+23.424785483973*(temperatura)-1093.53530316845

def calor_especifico(temperatura):
    # Retorna o valor do calor específico da água em kJ/kg K
    return 0.000000002784026*(temperatura**4)-0.000003736020793*(temperatura**3)+0.001884889509818*(temperatura**2)-0.42325554048777*(temperatura)+39.8390948742563

def viscosidade(temperatura):
    # Retorna a viscosidade da água em u Pa s 
    return 0.0000316379321*(temperatura**4)-0.0433590650205*(temperatura**3)+22.325809094914*(temperatura**2)-5124.88587735*(temperatura)+443419.505781729

def condutividade_termica(temperatura):
    # Retorna a condutividade térmica da água em J/s m K 
    return -0.0000000046*(temperatura**3)-0.0000051588*(temperatura**2)+0.0059627933*(temperatura)-0.5906098532

def pressao_vapor(temperatura):
    # Retorna a pressão de vapor da água em kPa
    return (101.325/760)*(e**(18.3036-(3816.44/(temperatura-46.13))))

if (__name__ == '__main__'):

    print('\n----- Calculadora de Propriedades Físicas da Água -----\n')

    while True:

        temperatura = int(input('Temperatura (°C): '))

        if temperatura < 0:
            print('\nA temperatura deve ser maior ou igual a 0°C\n')
        elif temperatura > 100:
            print('\nA temperatura deve ser menor ou igual a 100°C\n')
        else:
            temperatura +=  273.15

            while True:
                        
                print('1 - Densidade')
                print('2 - Calor Específico')
                print('3 - Viscosidade')
                print('4 - Condutividade Térmica')
                print('5 - Pressão de Vapor')
                print('6 - Todas')

                escolha = int(input('\nPropriedade Física: '))

                if escolha == 1:
                    print('\nA densidade da água na temperatura {} K é {} kg/m³\n'.format(temperatura, round(densidade(temperatura), 1)))
                    break
                elif escolha == 2:
                    print('\nO calor específico da água na temperatura {} K é {} kJ/kg K\n'.format(temperatura, round(calor_especifico(temperatura), 3)))
                    break
                elif escolha == 3:
                    print('\nA viscosidade da água na temperatura {} K é {} uPa s\n'.format(temperatura, round(viscosidade(temperatura), 1)))
                    break
                elif escolha == 4:
                    print('/nA condutividade térmica da água na temperatura {} K é {} J/s m K\n'.format(temperatura, round(condutividade_termica(temperatura), 4)))
                    break
                elif escolha == 5:
                    print('\nA pressão de vapor da água na temperatura {} K é {} kPa\n'.format(temperatura, round(pressao_vapor(temperatura), 1)))
                    break
                elif escolha == 6:
                    valores = [densidade(temperatura), calor_especifico(temperatura), viscosidade(temperatura), condutividade_termica(temperatura), pressao_vapor(temperatura)]
                    unidade = ['kg/m³', 'kJ/kg K', 'uPa s', 'J/s m K', 'kPa']
                    ind = ['Densidade', 'Calor Específico', 'Condutividade Térmica', 'Condutividade Térmica', 'Pressão de Vapor']
                    df = pd.DataFrame(data = list(zip(valores, unidade)), columns = ['Valor', 'Unidade'], index = ind)
                    print('\nPropriedades Físicas da Água na temperatura {} K\n'.format(temperatura))
                    print(df)
                    print('\n')
                    break
                else:
                    print('\nDigito Inválido\n')

            break           
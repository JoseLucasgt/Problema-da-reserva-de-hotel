# José Lucas Araújo dos Santos   13/05/2022   São Luis-Maranhão Brasil

import numpy as np
import datetime


def periodoDaSemana():
    """Verifica o periodo da semana"""

    # Verifica numero de diarias
    numeroDeDiarias = int(input('Indique o numero de dias que pretende ficar hospedado: '))
    print('o numero de diarias é de: ', numeroDeDiarias)
    vetorPeriodoDaSemana = []

    for i in range(numeroDeDiarias):

        # Verifica quais dias que o cliente pretende se hospedar
        print('\nDia ', i + 1, ':')
        dia = input('Digite o dia no formato DD/MM/YYYY: ')
        dia = datetime.datetime.strptime(dia, "%d/%m/%Y").date()
        periodoDaSemana = dia.weekday()

        # Verifica a cada dia se é meio da semana ou fim de semana
        if (periodoDaSemana == 5) or (periodoDaSemana == 6):  # 5 = Sábado, 6 = Domingo
            vetorPeriodoDaSemana.append(2)  # 2 = Fim de semana

        else:
            vetorPeriodoDaSemana.append(1)  # 1 = Dia da semana

    return numeroDeDiarias, vetorPeriodoDaSemana;


def orcamentoPorHotel(matrizClienteRegular, matrizClienteReward,
                      tipoDeCliente, numeroDeDiarias, vetorPeriodoDaSemana):
    """Criação de vetores com o orçamente diario para cada hotel"""

    hotelLakewood = [matrizClienteRegular[0]]
    hotelBridgewood = [matrizClienteRegular[2]]
    hotelRidgewood = [matrizClienteRegular[4]]

    # Faz orçamento caso o cliente for do tipo Regular
    if tipoDeCliente == 'Regular':  # tipo de cliente Regular
        for i in range(numeroDeDiarias):
            if vetorPeriodoDaSemana[i] == 1:  # Se é meio da semana
                hotelLakewood.append(matrizClienteRegular[1][0])
                hotelBridgewood.append(matrizClienteRegular[3][0])
                hotelRidgewood.append(matrizClienteRegular[5][0])

            else:  # Fim semana
                hotelLakewood.append(matrizClienteRegular[1][1])
                hotelBridgewood.append(matrizClienteRegular[3][1])
                hotelRidgewood.append(matrizClienteRegular[5][1])

    # Faz orçamento caso o cliente for do tipo Reward
    else:
        for i in range(numeroDeDiarias):
            if vetorPeriodoDaSemana[i] == 1:  # Se é meio da semana
                hotelLakewood.append(matrizClienteReward[1][0])
                hotelBridgewood.append(matrizClienteReward[3][0])
                hotelRidgewood.append(matrizClienteReward[5][0])

            else:  # Fim semana
                hotelLakewood.append(matrizClienteReward[1][1])
                hotelBridgewood.append(matrizClienteReward[3][1])
                hotelRidgewood.append(matrizClienteReward[5][1])
    return hotelLakewood, hotelBridgewood, hotelRidgewood


def CustoBeneficio(numeroDeDiarias, hotelLakewood, hotelBridgewood, hotelRidgewood):
    # Soma dos valores dos dias por hotel
    hotelLakewood.append(sum(hotelLakewood[1:numeroDeDiarias + 2]))
    hotelBridgewood.append(sum(hotelBridgewood[1:numeroDeDiarias + 2]))
    hotelRidgewood.append(sum(hotelRidgewood[1:numeroDeDiarias + 2]))

    # Calcula valor minimo
    menorValor = min(hotelLakewood[-1], hotelBridgewood[-1], hotelRidgewood[-1])

    # Verificação qual hotel com valor mínimo mais compensa
    if hotelRidgewood[-1] == menorValor:  # Hotel Ridgewood tem a melhor classificação
        recomendacao = hotelRidgewood[0]
    elif hotelBridgewood[-1] == menorValor:  # Hotel Brigewood tem a segunda melhor classificação
        recomendacao = hotelBridgewood[0]
    else:
        recomendacao = hotelLakewood[0]  # Hotel Lakewood tem a terceira melhor classificação

    print('Voce deve se hospedar no hotel: ', recomendacao)


def recomendacao(tipoDeCliente, numeroDeDiarias, vetorPeriodoDaSemana):
    """Verifica qual hotel tem o melhor custo benefício e faz recomendação"""

    # Diferentes tipos de clientes
    # Formato ---> 'NomeDoHotel', [valorNoMeioDaSemana, valorNoFimDeSemana]
    matrizClienteRegular = ['Lakewood', [110, 90],
                            'Bridgewood', [160, 60],
                            'Ridgewood', [220, 150]]

    matrizClienteReward = ['Lakewood', [80, 80],
                           'Bridgewood', [110, 50],
                           'Ridgewood', [100, 40]]

    # Orçamento diario por Hotel
    hotelLakewood, hotelBridgewood, hotelRidgewood = orcamentoPorHotel(matrizClienteRegular,
                                                                       matrizClienteReward, tipoDeCliente,
                                                                       numeroDeDiarias, vetorPeriodoDaSemana)

    # Verifica melhor custo benefício
    CustoBeneficio(numeroDeDiarias, hotelLakewood, hotelBridgewood, hotelRidgewood)


# Verifica tipo de cliente
tipoDeCliente = input('Bem vindo, digite se você é cliente Regular ou Reward: ')

# Verifica numero de diárias e periodo da semana (meio da semana ou fim de semana)
numeroDeDiarias, vetorPeriodoDaSemana = periodoDaSemana()

# Identifica qual o Hotel com melhor Custo benefício
recomendacao(tipoDeCliente, numeroDeDiarias, vetorPeriodoDaSemana)
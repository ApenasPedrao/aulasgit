# Aula 1 de física da primeira semana de estudos
def calc_velocidade_media(distancia, tempo):
    distancia = float (input("Digite a distância percorrida em metros: "))
    tempo = float(input("Digite o tempo gasto em segundos: "))

    velocidade = distancia / tempo
    print(f"A velocidade média é: {velocidade} m/s")


def calc_aceleracao_media(vel_inicial, vel_final, temp_inicial, temp_final):
    vel_inicial = float(input("Digite a velocidade inicial em m/s: "))
    vel_final = float(input("Digite a velocidade final em m/s: "))
    temp_inicial = float(input("Digite o tempo inicial em segundos: "))
    temp_final = float(input("Digite o tempo final em segundos: "))

    aceleracao = (vel_final - vel_inicial) / (temp_final - temp_inicial)
    print(f"A aceleração média é: {aceleracao} m/s²")


calc_velocidade_media(0,0)
calc_aceleracao_media(0,0,0,0)
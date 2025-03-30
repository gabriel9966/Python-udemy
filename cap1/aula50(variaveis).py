"""
constante = variáveis que não vao mudar
muitas condições no mesmo if é algo ruim
"""

velocidade = 61
local_carro = 101

#constantes
RADAR1 = 60
LOCAL1 = 100
RADAR_RANGE = 1

carro_multado = local_carro <= (local_carro + RADAR_RANGE) and \
      local_carro >= (local_carro - RADAR_RANGE)

if velocidade > RADAR1:
    print("Carro passou da velocidade do radar")

if carro_multado and velocidade > RADAR1:
    print('Carro multado')

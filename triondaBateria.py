# Entrada de dados
bateria_atual = int(input("Digite o nível da bateria (0 a 100): "))
bola_em_jogo = input("A bola está em jogo? (True/False): ") == "True"

# Processamento
if bateria_atual < 15 and bola_em_jogo:
    print("ALERTA MÁXIMO: Bateria baixa! Substitua a bola na próxima paralisação.")
elif bateria_atual < 15 and not bola_em_jogo:
    print("Aviso: Bateria baixa. Aproveite a bola parada para trocá-la.")
else:
    print("Sistema Trionda operando normalmente. Bateria ok.")

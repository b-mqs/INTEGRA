import os

# Votos para o primeiro grupo de candidatos
votos_Candidato1 = 0
votos_Candidato2 = 0
votos_Candidato3 = 0

# Votos para o segundo grupo de candidatos
votos_CandidatoA = 0
votos_CandidatoB = 0
votos_CandidatoC = 0

# Contadores de votantes
votantes_grupo1 = 0
votantes_grupo2 = 0

votacao_encerrada = False

while not votacao_encerrada:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Escolha o grupo de candidatos para votar:")
    print("1 - Grupo 1: Thiago(10), Junior(15), Rafael(20)")
    print("2 - Grupo 2: Ana(30), Beatriz(35), Carlos(40)")
    grupo = input("Digite o número do grupo (1 ou 2): ")

    if grupo == '1':
        print("-" * 30)
        print(f'Votos do Thiago(10): {votos_Candidato1}')
        print(f'Votos do Junior(15): {votos_Candidato2}')
        print(f'Votos do Rafael(20): {votos_Candidato3}')
        print("-" * 30)
        
        try:
            voto = int(input("Em quem você deseja votar? "))
            if voto == 10:
                votos_Candidato1 += 1
                votantes_grupo1 += 1
            elif voto == 15:
                votos_Candidato2 += 1
                votantes_grupo1 += 1
            elif voto == 20:
                votos_Candidato3 += 1
                votantes_grupo1 += 1
            else:
                print("Número de candidato inválido.")
        except ValueError:
            print("Digite apenas os números dos candidatos.")

    elif grupo == '2':
        print("-" * 30)
        print(f'Votos da Ana(30): {votos_CandidatoA}')
        print(f'Votos da Beatriz(35): {votos_CandidatoB}')
        print(f'Votos do Carlos(40): {votos_CandidatoC}')
        print("-" * 30)
        
        try:
            voto = int(input("Em quem você deseja votar? "))
            if voto == 30:
                votos_CandidatoA += 1
                votantes_grupo2 += 1
            elif voto == 35:
                votos_CandidatoB += 1
                votantes_grupo2 += 1
            elif voto == 40:
                votos_CandidatoC += 1
                votantes_grupo2 += 1
            else:
                print("Número de candidato inválido.")
        except ValueError:
            print("Digite apenas os números dos candidatos.")

    else:
        print("Grupo inválido. Digite apenas 1 ou 2.")
        continue

    encerramento = input("Deseja encerrar a votação agora? (Sim/Não): ")
    if encerramento.lower() == "sim":
        os.system('cls' if os.name == 'nt' else 'clear')

        # Resultados do Grupo 1
        print("Resultados do Grupo 1:")
        if votos_Candidato1 > votos_Candidato2 and votos_Candidato1 > votos_Candidato3:
            print(f'Thiago ganhou a eleição com {votos_Candidato1} votos dentre os {votantes_grupo1} eleitores.')
        elif votos_Candidato2 > votos_Candidato1 and votos_Candidato2 > votos_Candidato3:
            print(f'Junior ganhou a eleição com {votos_Candidato2} votos dentre os {votantes_grupo1} eleitores.')
        elif votos_Candidato3 > votos_Candidato1 and votos_Candidato3 > votos_Candidato2:
            print(f'Rafael ganhou a eleição com {votos_Candidato3} votos dentre os {votantes_grupo1} eleitores.')
        else:
            print(f'Houve um empate no Grupo 1. Thiago: {votos_Candidato1}, Junior: {votos_Candidato2}, Rafael: {votos_Candidato3} votos.')

        # Resultados do Grupo 2
        print("\nResultados do Grupo 2:")
        if votos_CandidatoA > votos_CandidatoB and votos_CandidatoA > votos_CandidatoC:
            print(f'Ana ganhou a eleição com {votos_CandidatoA} votos dentre os {votantes_grupo2} eleitores.')
        elif votos_CandidatoB > votos_CandidatoA and votos_CandidatoB > votos_CandidatoC:
            print(f'Beatriz ganhou a eleição com {votos_CandidatoB} votos dentre os {votantes_grupo2} eleitores.')
        elif votos_CandidatoC > votos_CandidatoA and votos_CandidatoC > votos_CandidatoB:
            print(f'Carlos ganhou a eleição com {votos_CandidatoC} votos dentre os {votantes_grupo2} eleitores.')
        else:
            print(f'Houve um empate no Grupo 2. Ana: {votos_CandidatoA}, Beatriz: {votos_CandidatoB}, Carlos: {votos_CandidatoC} votos.')

        votacao_encerrada = True
    else:
        votacao_encerrada = False

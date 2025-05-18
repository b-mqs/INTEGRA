import os


votos_Candidato1 = 0
votos_Candidato2 = 0
votos_Candidato3 = 0
votantes = 0

votacao_encerrada = False

while votacao_encerrada == False:
    print("-" * 30)
    print(f'Votos do Candidato1(Thiago(10)): {votos_Candidato1}')
    print(f'Votos do Candidato2(Junior(15)): {votos_Candidato2}')
    print(f'Votos do Candidato3(Rafael(20)): {votos_Candidato3}')
    print("-" * 30)
    
    voto = int(input("Em quem você deseja votar? (Os nomes dos candidatos estarão disponivel para consulta): "))
    
    try:
        if voto == 10:
            votos_Candidato1 += 1
            votantes += 1
        elif voto == 15:
            votos_Candidato2 += 1
            votantes += 1
        elif voto == 20:
            votos_Candidato3 += 1
            votantes += 1
        else:
            pass
    except:
        print("Digite apenas os numeros dos candidadtos, Digitando os nomes os votos não serão computados.")   
    
    encerramento = input("Deseja encerrar a votação agora? (Sim/Não)")
    if encerramento == "Sim":
        os.system('cls')
        if votos_Candidato1 - votos_Candidato2 - votos_Candidato3 >= 1 or votos_Candidato1 > votos_Candidato2 and votos_Candidato3:
               print(f'Thiago ganhou a eleição com {votos_Candidato1} votos dentre os {votantes} eleitores')
        elif votos_Candidato1 - votos_Candidato2 - votos_Candidato3 >= 1 or votos_Candidato2 > votos_Candidato1 and votos_Candidato3:
               print(f'Junior ganhou a eleição com {votos_Candidato2} votos dentre os {votantes} eleitores')
        elif votos_Candidato1 - votos_Candidato2 - votos_Candidato3 >= 1 or votos_Candidato3 > votos_Candidato2 and votos_Candidato3:
                 print(f'Rafael ganhou a eleição com {votos_Candidato3} votos dentre os {votantes} eleitores')

        else:
            print(f'Houve um empate:  O candidato Thiago obteve {votos_Candidato1} votos, o candidato Junior obteve {votos_Candidato2} votos, o candidato Rafael obteve {votos_Candidato3} votos')
            print(f'Houveram {votantes} votos dos eleitores')
            print("A votação está encerrada.")
            votacao_encerrada = True
            
    else:
        os.system('cls')
        votacao_encerrada = False 
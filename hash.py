import os
import hashlib
import getpass
import sqlite3

# Conecta ao banco de dados SQLite ou cria um novo se não existir
conn = sqlite3.connect('votacao.db')
cursor = conn.cursor()

# Cria a tabela para armazenar usuários, caso ainda não exista
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    cpf TEXT PRIMARY KEY,
    senha_hash TEXT NOT NULL
)
""")
conn.commit()

def hash_password(password):
    """ Retorna o hash da senha usando SHA-256 """
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario():
    """ Registra um novo usuário com CPF e senha """
    cpf = input("Digite seu CPF (11 dígitos) para registro: ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve conter exatamente 11 dígitos.")
        return False
    
    senha = getpass.getpass("Digite sua senha para registro: ")
    senha_hash = hash_password(senha)
    
    try:
        cursor.execute("""
        INSERT INTO usuarios (cpf, senha_hash) VALUES (?, ?)
        """, (cpf, senha_hash))
        conn.commit()
        print("Registro realizado com sucesso!")
        return True
    except sqlite3.IntegrityError:
        print("Este CPF já está registrado.")
        return False

def validar_login():
    """ Valida o login do usuário """
    cpf = input("Digite seu CPF (11 dígitos): ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido.")
        return None
    
    cursor.execute("SELECT senha_hash FROM usuarios WHERE cpf = ?", (cpf,))
    usuario = cursor.fetchone()
    if usuario is None:
        print("CPF não registrado.")
        return None
    
    senha = getpass.getpass("Digite sua senha: ")
    senha_hash = hash_password(senha)
    
    if usuario[0] != senha_hash:
        print("Senha incorreta.")
        return None
    
    return cpf

votos_Candidato1 = 0
votos_Candidato2 = 0
votos_Candidato3 = 0

votos_CandidatoA = 0
votos_CandidatoB = 0
votos_CandidatoC = 0


votantes_grupo1 = 0
votantes_grupo2 = 0


usuarios_registrados = {}
votou_grupo1 = {}
votou_grupo2 = {}

# Primeiro, perguntamos se o usuário deseja se registrar
print("Bem-vindo ao sistema de votação!")
registrar = input("Deseja registrar um novo usuário? (Sim/Não): ")
if registrar.lower() == "sim":
    while True:
        sucesso = registrar_usuario()
        if not sucesso:
            continuar = input("Deseja tentar registrar novamente? (Sim/Não): ")
            if continuar.lower() != "sim":
                break
        else:
            break

votacao_encerrada = False

while not votacao_encerrada:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Faça login para votar ou registre-se:")
    
    # Validação do login do usuário
    usuario_cpf = validar_login()
    
    if usuario_cpf is None:
        # Oferece ao usuário a opção de se registrar após falha no login
        tentar_registrar = input("CPF não registrado ou senha incorreta. Deseja se registrar? (Sim/Não): ")
        if tentar_registrar.lower() == "sim":
            sucesso = registrar_usuario()
            if sucesso:
                # Tenta fazer login novamente após registro bem-sucedido
                usuario_cpf = validar_login()
                if usuario_cpf is None:
                    continue  # Retorna ao início do loop principal se o login falhar novamente
        else:
            continue  # Retorna ao início do loop principal

    print("Login realizado com sucesso!")
    
    while True:  # Loop interno para seleção de grupo e voto
        print("Escolha o grupo de candidatos para votar:")
        print("1 - Professores: Thiago(10), Junior(15), Rafael(20)")
        print("2 - Funcionarios: Ana(30), Beatriz(35), Carlos(40)")
        print("3 - Sair e não votar em mais ninguém")
        
        grupo = input("Digite o número do grupo (1 ou 2): ")

        if grupo == '1':
            if usuario_cpf in votou_grupo1:
                print("Você já votou neste grupo.")
                continue
        
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
                    continue
            except ValueError:
                print("Digite apenas os números dos candidatos.")
                continue
            
            votou_grupo1[usuario_cpf] = True

        elif grupo == '2':
            if usuario_cpf in votou_grupo2:
                print("Você já votou neste grupo.")
                continue
        
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
                    continue
            except ValueError:
                print("Digite apenas os números dos candidatos.")
                continue
            
            votou_grupo2[usuario_cpf] = True

        elif grupo == '3':
            break  # Sai do loop interno sem votar novamente

        else:
            print("Grupo inválido. Digite apenas 1, 2 ou 3.")
            continue

        # Pergunta se deseja encerrar a votação
        encerramento = input("Deseja encerrar a votação agora? (Sim/Não): ")
        if encerramento.lower() == "sim":
            os.system('cls' if os.name == 'nt' else 'clear')

            # Resultados do Grupo 1
            total_votos_grupo1 = votos_Candidato1 + votos_Candidato2 + votos_Candidato3
            if total_votos_grupo1 > 0:
                print("Resultados dos Professores:")
                print(f'Thiago(10): {votos_Candidato1 / total_votos_grupo1 * 100:.2f}%')
                print(f'Junior(15): {votos_Candidato2 / total_votos_grupo1 * 100:.2f}%')
                print(f'Rafael(20): {votos_Candidato3 / total_votos_grupo1 * 100:.2f}%')

            # Resultados do Grupo 2
            total_votos_grupo2 = votos_CandidatoA + votos_CandidatoB + votos_CandidatoC
            if total_votos_grupo2 > 0:
                print("\nResultados do Funcionarios:")
                print(f'Ana(30): {votos_CandidatoA / total_votos_grupo2 * 100:.2f}%')
                print(f'Beatriz(35): {votos_CandidatoB / total_votos_grupo2 * 100:.2f}%')
                print(f'Carlos(40): {votos_CandidatoC / total_votos_grupo2 * 100:.2f}%')

            votacao_encerrada = True
            break  # Sai do loop interno

        else:
            print("Continuando a votação...")
            # Retorna para a seleção de grupo sem sair do loop principal


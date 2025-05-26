import os
import hashlib
import getpass
import sqlite3
import msvcrt


conn = sqlite3.connect('votacao.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    cpf TEXT PRIMARY KEY,
    senha_hash TEXT NOT NULL
)
""")
conn.commit()


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario():
    """ Handles user registration screen """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Tela de Registro de Usuário ---")
    cpf = input("Digite seu CPF (11 dígitos) para registro: ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido. Deve conter exatamente 11 dígitos.")
        input("Pressione Enter para continuar...")
        return False

    while True:
        senha = getpass.getpass("Digite sua senha para registro (mínimo de 6 caracteres): ")
        if len(senha) < 6:
            print("A senha deve ter no mínimo 6 caracteres. Tente novamente.")
            continue
        senha_hash = hash_password(senha)

        try:
            cursor.execute("""
            INSERT INTO usuarios (cpf, senha_hash) VALUES (?, ?)
            """, (cpf, senha_hash))
            conn.commit()
            print("Registro realizado com sucesso!")
            input("Pressione Enter para continuar...")
            return True
        except sqlite3.IntegrityError:
            print("Este CPF já está registrado no sistema. Por favor, tente fazer login ou use outro CPF para se registrar.")
            if input("Deseja tentar registrar novamente? (Sim/Não): ").lower() != "sim":
                return False
            else:
            
                cpf = input("Digite outro CPF (11 dígitos) para registro: ")
                if not cpf.isdigit() or len(cpf) != 11:
                    print("CPF inválido. Voltando ao menu principal.")
                    input("Pressione Enter para continuar...")
                    return False


def validar_login():
    """ Handles user login screen """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Tela de Login ---")
    cpf = input("Digite seu CPF (11 dígitos): ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("CPF inválido.")
        input("Pressione Enter para continuar...")
        return None

    cursor.execute("SELECT senha_hash FROM usuarios WHERE cpf = ?", (cpf,))
    usuario = cursor.fetchone()
    if usuario is None:
        print("CPF não registrado.")
        input("Pressione Enter para continuar...")
        return None

    senha = getpass.getpass("Digite sua senha: ")
    senha_hash = hash_password(senha)

    if usuario[0] != senha_hash:
        print("Senha incorreta.")
        input("Pressione Enter para continuar...")
        return None
    else:
        print("Login bem-sucedido!")
        input("Pressione Enter para continuar...")
        return cpf


votos_Candidato1 = 0
votos_Candidato2 = 0
votos_Candidato3 = 0
votos_CandidatoA = 0
votos_CandidatoB = 0
votos_CandidatoC = 0
votantes_grupo1 = 0
votantes_grupo2 = 0
votou_grupo1 = {} 
votou_grupo2 = {} 


def votar(usuario_cpf):
    """ Handles the voting screen after successful login """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"--- Tela de Votação para {usuario_cpf} ---")
        print("\nEscolha o grupo de candidatos para votar:")
        print("1 - Professores: Thiago(10), Junior(15), Rafael(20)")
        print("2 - Funcionários: Ana(30), Beatriz(35), Carlos(40)")
        print("3 - Sair e não votar em mais ninguém")

        grupo = input("Digite o número do grupo (1, 2 ou 3): ")

        if grupo == '3':
            break
        elif grupo == '1':
            if usuario_cpf in votou_grupo1:
                print("Você já votou neste grupo.")
                input("Pressione Enter para continuar...")
                continue 
            realizar_voto_grupo(grupo, usuario_cpf)
        elif grupo == '2':
            if usuario_cpf in votou_grupo2:
                print("Você já votou neste grupo.")
                input("Pressione Enter para continuar...")
                continue 
            realizar_voto_grupo(grupo, usuario_cpf)
        else:
            print("Grupo inválido. Digite apenas 1, 2 ou 3.")
            input("Pressione Enter para continuar...")

def realizar_voto_grupo(grupo, usuario_cpf):
    global votos_Candidato1, votos_Candidato2, votos_Candidato3
    global votos_CandidatoA, votos_CandidatoB, votos_CandidatoC
    global votantes_grupo1, votantes_grupo2

    os.system('cls' if os.name == 'nt' else 'clear') 
    if grupo == '1':
        print("--- Votação: Grupo de Professores ---")
        print("-" * 30)
        print(f'Votos do Thiago(10): {votos_Candidato1}')
        print(f'Votos do Junior(15): {votos_Candidato2}')
        print(f'Votos do Rafael(20): {votos_Candidato3}')
        print("-" * 30)

        try:
            voto = int(input("Em quem você deseja votar? "))
            if voto == 10:
                votos_Candidato1 += 1
            elif voto == 15:
                votos_Candidato2 += 1
            elif voto == 20:
                votos_Candidato3 += 1
            else:
                print("Número de candidato inválido. Tente novamente.")
                input("Pressione Enter para continuar...")
                return
        except ValueError:
            print("Entrada inválida. Digite apenas os números dos candidatos.")
            input("Pressione Enter para continuar...")
            return

        votou_grupo1[usuario_cpf] = True
        votantes_grupo1 += 1
        print("Voto registrado com sucesso para o grupo de Professores!")

    elif grupo == '2':
        print("--- Votação: Grupo de Funcionários ---")
        print("-" * 30)
        print(f'Votos da Ana(30): {votos_CandidatoA}')
        print(f'Votos da Beatriz(35): {votos_CandidatoB}')
        print(f'Votos do Carlos(40): {votos_CandidatoC}')
        print("-" * 30)

        try:
            voto = int(input("Em quem você deseja votar? "))
            if voto == 30:
                votos_CandidatoA += 1
            elif voto == 35:
                votos_CandidatoB += 1
            elif voto == 40:
                votos_CandidatoC += 1
            else:
                print("Número de candidato inválido. Tente novamente.")
                input("Pressione Enter para continuar...")
                return
        except ValueError:
            print("Entrada inválida. Digite apenas os números dos candidatos.")
            input("Pressione Enter para continuar...")
            return

        votou_grupo2[usuario_cpf] = True
        votantes_grupo2 += 1
        print("Voto registrado com sucesso para o grupo de Funcionários!")
    input("Pressione Enter para continuar...") 
    
    
def encerrar_votacao():
    """ Displays the final voting results screen """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Resultados Finais da Votação ---")
    print("Votação encerrada. Aqui estão os resultados:")

    total_votos_grupo1 = votos_Candidato1 + votos_Candidato2 + votos_Candidato3
    if total_votos_grupo1 > 0:
        print("\n--- Resultados dos Professores ---")
        print(f'Thiago(10): {votos_Candidato1} votos ({votos_Candidato1 / total_votos_grupo1 * 100:.2f}%)')
        print(f'Junior(15): {votos_Candidato2} votos ({votos_Candidato2 / total_votos_grupo1 * 100:.2f}%)')
        print(f'Rafael(20): {votos_Candidato3} votos ({votos_Candidato3 / total_votos_grupo1 * 100:.2f}%)')
    else:
        print("\n--- Nenhum voto registrado para o grupo de Professores. ---")


    total_votos_grupo2 = votos_CandidatoA + votos_CandidatoB + votos_CandidatoC
    if total_votos_grupo2 > 0:
        print("\n--- Resultados dos Funcionários ---")
        print(f'Ana(30): {votos_CandidatoA} votos ({votos_CandidatoA / total_votos_grupo2 * 100:.2f}%)')
        print(f'Beatriz(35): {votos_CandidatoB} votos ({votos_CandidatoB / total_votos_grupo2 * 100:.2f}%)')
        print(f'Carlos(40): {votos_CandidatoC} votos ({votos_CandidatoC / total_votos_grupo2 * 100:.2f}%)')
    else:
        print("\n--- Nenhum voto registrado para o grupo de Funcionários. ---")

    input("\nPressione Enter para voltar ao menu principal...")


def menu_principal():
    """ Main menu and navigation between screens """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("--- Sistema de Votação ---")
        print("Menu Principal:")
        print("1 - Registrar novo usuário")
        print("2 - Fazer login e votar")
        print("3 - Encerrar votação e ver resultados")
        print("4 - Sair do sistema")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_usuario() 
        elif opcao == '2':
            usuario_cpf = validar_login() 
            if usuario_cpf: 
                votar(usuario_cpf)
        elif opcao == '3':
            encerrar_votacao() 
            break 
        elif opcao == '4':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    menu_principal()
    conn.close()
    print("Conexão com o banco de dados fechada.")
import time
def introducao():
    print("\nBem-vindo ao Reino de Veridia.")
    print("O necromante Malkor ameaça destruir tudo. Você é um dos poucos sobreviventes de sua vila.")
    print("Para derrotá-lo, você precisa encontrar a arma lendária.")
    time.sleep(3)
    escolha_personagem()


def escolha_personagem():
    print("\nEscolha seu personagem:")
    print("1 - Mago (Poder mágico)")
    print("2 - Guerreiro (Força bruta)")
    print("3 - Arqueiro (Agilidade e precisão)")
    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == "1":
        personagem = "Mago"
    elif escolha == "2":
        personagem = "Guerreiro"
    elif escolha == "3":
        personagem = "Arqueiro"
    else:
        print("Opção inválida. Tente novamente.")
        return escolha_personagem()
    
    print(f"\nVocê escolheu ser um {personagem}.")
    time.sleep(1)
    escolha_caminho(personagem)
print ('agora você deve decidir como buscar a arma lendária')
print ('1 - A Aliança Secreta (Estudar magia proibida')
print ('2 - A Força Bruta (Treinar com guerreiros experientes')
 escolha = input('Digite 1 ou 2: ')
 if escolha == '1':
     aliança_secreta(personagem)
 elif escolha == '2':
     forca_brita(personagem)
else :
print('Opção invalida. Tente novamente')
escolha_caminho(personagem)

def aliança_secreta(personagem):
    print("\nVocê treina com guerreiros da resistência.")
    print("Aprende táticas de combate e se prepara para enfrentar Malkor.")
    time.sleep(2)
    labirinto_sombrio(personagem)

 def forca_bruta(personagem):
    print("\nVocê treina com guerreiros da resistência.")
    print("Aprende táticas de combate e se prepara para enfrentar Malkor.")
    time.sleep(2)
    labirinto_sombrio(personagem)

def floresta_ilusoes(personagem):
    print("\nVocê entra na Floresta das Ilusões. O caminho muda constantemente.")
    print("Escolha como navegar:")
    print("1 - Seguir os sussurros misteriosos")
    print("2 - Confiar apenas nos seus instintos")
    escolha = input("Digite 1 ou 2: ")

  if escolha == "1":
        print("\nOs sussurros revelam um caminho oculto e você sai da floresta ileso.")
        time.sleep(2)
        deserto_guardiao(personagem)
    elif escolha == "2":
        print("\nA floresta te confunde, e você perde tempo precioso.")
        time.sleep(2)
        deserto_guardiao(personagem)
    else:
        print("Opção inválida. Tente novamente.")
        floresta_ilusoes(personagem)
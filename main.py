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

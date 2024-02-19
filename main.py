def adicionar_contato(contatos, nome_contato,telefone_contato,email_contato):
    contato= {"contato": nome_contato,"telefone":telefone_contato,
              "email":email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
 
def ver_contatos(contatos):
    if len(contatos) > 0: 
        for indice, contato in enumerate(contatos, start=1):
            status= "✓" if contato["favorito"] else ""
            nome_contato= contato["contato"]
            telefone_contato= contato["telefone"]
            email_contato= contato["email"]
            print(f" {indice}. [{status}] {nome_contato} {telefone_contato} {email_contato}")
    else:
        print("Ainda não há contatos cadastrados!")

def editar_contato(contatos, indice_contato, novo_nome_contato):
    indice_contato_ajustado = int(indice_contato) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
        print(f"Contato {indice_contato} atualizado(a) para {novo_nome_contato}")
        escolha= input("Deseja alterar algum outro campo (S/N)?")

        if escolha == 'S':
            sim=input("Qual campo você quer editar: ")
            if sim=='telefone':
                try:
                    novo_telefone = int(input("Digite o novo telefone do contato: "))
                    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
                    print(f"Contato {indice_contato} atualizado(a) para {novo_telefone}")       
                except ValueError as e:
                    print(f"Erro de value error: {e}")
                    raise ValueError("Tipo de variaveis incompativeis. Digite um numero de telefone!")
            elif sim=='email':
                novo_email = input("Digite o novo email do contato: ")
                contatos[indice_contato_ajustado]["email"] = novo_email
                print(f"Contato {indice_contato} atualizado(a) para {novo_email}")
        else:
            return
    else:
        print("Índice de contato inválido.")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    else:
        print("Índice de contato inválido.")

def desfavoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} desmarcado como favorito")
    else:
        print("Índice de contato inválido.")

def excluir_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print(f"Contato {indice_contato} excluido com sucesso")
    else:
        print("Índice de contato inválido.")

contatos= []

while True:
    print("Bem vindo ao Contatos")
    print("1- Adicionar novo contato")
    print("2- Ver contatos")
    print("3- Editar contato")
    print("4- Marcar contato como favorito")
    print("5- Desmarcar contato como favorito")
    print("6- Excluir contato")
    print("7- Sair")

    try:
        escolha = int(input("Digite sua escolha:"))

        if escolha == "1":
            nome_contato= input("Digite o nome do contato: ")
            telefone_contato= input("Digite o telefone do contato: ")
            email_contato= input("Digite o email do contato: ")
            adicionar_contato(contatos, nome_contato,telefone_contato,email_contato)

        elif escolha == "2":
            ver_contatos(contatos)
        
        elif escolha=="3":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja atualizar: ")
            novo_nome = input("Digite o novo nome do contato: ")
            editar_contato(contatos, indice_contato, novo_nome)

        elif escolha=="4":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja favoritar: ")
            favoritar_contato(contatos, indice_contato)

        elif escolha=="5":
            ver_contatos(contatos)
            indice_contato = input("Digite o número do contato que deseja desfavoritar: ")
            desfavoritar_contato(contatos, indice_contato)

        elif escolha=="6":
            ver_contatos(contatos)
            nome_contato = input("Digite o número do contato que deseja excluir: ")
            excluir_contato(contatos, nome_contato)

        elif escolha== "7":
            break 
        
    except ValueError as e:
        print(f"Erro de value error: {e}")
        raise ValueError("Tipo de variaveis incompativeis. Digite um numero de 1 a 6!")

    print("Programa finalizado!")

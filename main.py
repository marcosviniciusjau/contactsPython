def adicionar_contato(contatos, nome_contato,telefone_contato,email_contato):
    contato= {"contato": nome_contato,"telefone":telefone_contato,"email":email_contato, "favorito": False}
    contatos.append(contato)
    print(f"O contato {nome_contato} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    for indice, contato in enumerate(contatos, start=1):
        status= "✓" if contato["favorito"] else ""
        nome_contato= contato["contato"]
        telefone_contato= contato["telefone"]
        email_contato= contato["email"]
        print(f" {indice}. [{status}] {nome_contato} {telefone_contato} {email_contato}")

def editar_contato(contatos, indice_contato, novo_nome_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["contato"] = novo_nome_contato
    print(f"Contato {indice_contato} atualizado(a) para {novo_nome_contato}")
    escolha= input("Deseja alterar algum outro campo (S/N)?")
    if(escolha == 'S'){
       input("")
    }
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
  return

def desfavoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["favorito"] = False
    print(f"Contato {indice_contato} desmarcado como favorito")
  else:
    print("Índice de contato inválido.")
  return


def excluir_contato(contatos, indice_contato):
     indice_contato_ajustado = int(indice_contato) - 1
     if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos.pop(indice_contato_ajustado)
        print(f"Contato {indice_contato} excluido com sucesso")
     else:
        print("Índice de contato inválido.")
     return

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

    escolha = input("Digite sua escolha:")

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

    print("Programa finalizado!")
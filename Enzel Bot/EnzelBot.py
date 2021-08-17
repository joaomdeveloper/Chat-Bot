import funcionalidades
import os

funcionalidades.PaginaApresentacao()
nomeDoUsuario = input("Apresente seu nome para o Enzel Bot: ")
chatDoBot = "Voltar"
while chatDoBot == "Voltar":
    acessarChatBot = input("Para entrar no chat, digite 'EZB': ")

    if acessarChatBot == "EZB":
        conversaChatBot = "PGN"
        while conversaChatBot == "PGN":
            funcionalidades.ChatBotEnzel()
            perguntaDoUsuario = input(f'{nomeDoUsuario}: ')
            
            #SESSÃO - VALE APENA APRENDER PYTHON
            if perguntaDoUsuario == "Vale apena aprender Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaValeApenaAprenderPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "vale apena aprender python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaValeApenaAprenderPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "VALE APENA APRENDER PYTHON?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaValeApenaAprenderPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "Vale apena aprender python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaValeApenaAprenderPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")
            #SESSÃO - VALE APENA APRENDER PYTHON


            #SESSÃO - OQUE É PYTHON
            elif perguntaDoUsuario == "Oque é Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueEoPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "OQUE É PYTHON?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueEoPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "oque é python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueEoPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")
            
            elif perguntaDoUsuario == "Oque é python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueEoPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")
            #SESSÃO - OQUE É PYTHON

            #SESSÃO - OQUE É POSSÍVEL FAZER COM PYTHON
            elif perguntaDoUsuario == "Oque fazer com Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueFazerComPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "Oque é possível fazer com Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueFazerComPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "Oque posso fazer com Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOqueEoPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")
            #SESSÃO - OQUE É POSSÍVEL FAZER COM PYTHON

            #SESSÃO - ONDE BAIXAR O PYTHON
            elif perguntaDoUsuario == "Onde baixar o Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaOndeBaixarPython()
                perguntaDownloadPython = input(f'{nomeDoUsuario}: ')

                if perguntaDownloadPython == "Sim":
                    os.startfile('www.python.org/downloads')
                    conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

                else:
                    print("\n")
                    print("Enzel Bot:")
                    print("É uma pena! Bom, fique á vontade para continuar a conversa.")
                    conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            #SESSÃO - ONDE BAIXAR O PYTHON
            elif perguntaDoUsuario == "Quais empresas usam Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaQuaisEmpresasUtilizamPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "Qual empresa usa python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaQuaisEmpresasUtilizamPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")

            elif perguntaDoUsuario == "Qual empresa utiliza Python?":
                print("\n")
                print("Enzel Bot:")
                funcionalidades.PerguntaQuaisEmpresasUtilizamPython()
                conversaChatBot = input("Para retornar a conversa digite 'PGN': ")
            #SESSÃO - ONDE BAIXAR O PYTHON

            else:
                os.system('cls')
                funcionalidades.PalavraNaoEncontrada()
                conversaChatBot = input("Para tentar novamente digite 'PNG': ")
    else:
        os.system('cls')
        funcionalidades.TentarEntrarNovamente()
        print("Não foi possível permitir a sua entrada ao chat, certfique-se de ter digitado o nome corretamente!")
        chatDoBot = input("Para tentar novamente digite 'Voltar': ")
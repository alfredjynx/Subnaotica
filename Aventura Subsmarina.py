# import random
# tesouros_lista = [3,4,1,2]
# def calcula_tesouros(tesouro,lista):
#     print("Deseja se livrar de algum tesouro ou vasculhar por novos? Pressione [v] para VASCULHAR ou [l] para LARGAR" )
#     player_input = input("Nos diga sua escolha, ó corajoso mergulhador: ")
#     if player_input == "v":
#         tesouro_vasculhado = random.randint(1,3)
#         num_tesouros = len(lista)
#         if num_tesouros>3:
#             print("Suas forças permitem apenas 4 tesouros, e você deseja adicionar mais um? Escolha um para ser substituído")
#             print(lista)
#             print("1   2   3   4")
#             escolha_despejar = int(input("Escolha aqui qual tesouro deverá ser despejado no Oceano, seu maníaco"))

maiornum = 0
num = 1
while num>0:
    num = float(input("Escolha um número: "))
    if num>maiornum:
        maiornum = num
print(maiornum)


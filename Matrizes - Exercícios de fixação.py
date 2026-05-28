import numpy as np
code = int(input("choose your exercise (1-20)\n"))

if code == 1:
    manha = np.random.randint(0, 51, size=(3, 3))

    tarde = np.random.randint(0, 51, size=(3, 3))

    soma = (manha + tarde)
    print("Manha: \n", manha, "\n")
    print("Tarde: \n", tarde, "\n")
    print("Total: \n", soma, "\n")

elif code == 2:
    estoque_inicial = np.random.randint(0, 101, size=(3, 3))

    vendidos = np.random.randint(0, 101, size=(3, 3))

    estoque_final = (estoque_inicial - vendidos)
    print("estoque inicial: \n", estoque_inicial, "\n")
    print("vendidos: \n", vendidos, "\n")
    print("estoque final: \n", estoque_final, "\n")

elif code == 3:
    ingredientes = np.random.randint(0, 21, size=(3, 3))

    pedidos = np.random.randint(0, 21, size=(3, 3))

    total = np.dot(ingredientes, pedidos)
    print("Total de produtos: \n", total, "\n")

elif code == 4:
    salarios = np.random.randint(1000, 3001, size=(3, 3))

    salarios_ajuste = (salarios * 1.10)
    print("salarios iniciais: \n", salarios, "\n")
    print("salarios ajustados: \n", salarios_ajuste, "\n")

elif code == 5:
    dados = np.random.rand(3, 3)
    dados = np.zeros(dados.shape)
    print(dados)

elif code == 6:
    dados = np.random.rand(4, 4)
    dados = np.ones(dados.shape)
    print(dados)

elif code == 7:
    matriz =np.array([
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25] ])
    print("Matriz original:\n", matriz, "\n")

    matriz[0][1] = 99
    matriz[2][4] = 99

    print("Matriz modificada:\n", matriz, "\n")


else:
    print("Type a valid exercise")
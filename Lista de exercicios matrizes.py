import random

code = int(input("choose your exercise (1-15)\n"))

if code == 1:
    matriz = []
    print("Digite os 9 elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    total = sum(matriz[i][j] for i in range(3) for j in range(3))
    print(f"Soma total dos elementos: {total}")

elif code == 2:
    n = int(input("Digite o valor de n para a Matriz Identidade: "))
    identidade = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    print(f"Matriz Identidade {n}x{n}:")
    for linha in identidade:
        print(linha)

elif code == 3:
    matriz = []
    print("Digite os 16 elementos da matriz 4x4:")
    for i in range(4):
        linha = []
        for j in range(4):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    numero = int(input("Digite o número a buscar: "))
    encontrado = any(matriz[i][j] == numero for i in range(4) for j in range(4))
    if encontrado:
        print(f"O número {numero} está na matriz.")
    else:
        print(f"O número {numero} NÃO está na matriz.")

elif code == 4:
    matriz = []
    print("Digite os 4 elementos da matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    print("Matriz original:")
    for linha in matriz:
        print(linha)
    matriz[0], matriz[1] = matriz[1], matriz[0]
    print("Matriz após troca das linhas:")
    for linha in matriz:
        print(linha)

elif code == 5:
    matriz = []
    print("Digite os 9 elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            val = float(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    escalar = float(input("Digite o escalar: "))
    resultado = [[matriz[i][j] * escalar for j in range(3)] for i in range(3)]
    print("Matriz resultante:")
    for linha in resultado:
        print(linha)

elif code == 6:
    matriz = []
    print("Digite os 12 elementos da matriz 3x4:")
    for i in range(3):
        linha = []
        for j in range(4):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    pares = sum(1 for i in range(3) for j in range(4) if matriz[i][j] % 2 == 0)
    print(f"Quantidade de números pares na matriz: {pares}")

elif code == 7:
    linhas = int(input("Número de linhas da matriz: "))
    colunas = int(input("Número de colunas da matriz: "))
    matriz = [[random.randint(1, 100) for _ in range(colunas)] for _ in range(linhas)]
    print("Matriz gerada:")
    for linha in matriz:
        print(linha)
    maior = max(matriz[i][j] for i in range(linhas) for j in range(colunas))
    print(f"Maior elemento da matriz: {maior}")

elif code == 8:
    matriz = []
    print("Digite os 9 elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            val = float(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    print("Médias por linha:")
    for i, linha in enumerate(matriz):
        media = sum(linha) / len(linha)
        print(f"  Linha {i}: {media:.2f}")

elif code == 9:
    matriz = []
    print("Digite os 16 elementos da matriz 4x4:")
    for i in range(4):
        linha = []
        for j in range(4):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    soma_diagonal = sum(matriz[i][i] for i in range(4))
    print(f"Soma da diagonal principal: {soma_diagonal}")

elif code == 10:
    m = int(input("Número de linhas (M): "))
    n = int(input("Número de colunas (N): "))
    matriz = []
    print(f"Digite os elementos da matriz {m}x{n}:")
    for i in range(m):
        linha = []
        for j in range(n):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    transposta = [[matriz[i][j] for i in range(m)] for j in range(n)]
    print(f"Matriz transposta {n}x{m}:")
    for linha in transposta:
        print(linha)

elif code == 11:
    matriz = []
    print("Digite os 9 elementos da matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    soma_colunas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]
    print(f"Soma de cada coluna: {soma_colunas}")

elif code == 12:
    n = int(input("Ordem da matriz quadrada: "))
    matriz = []
    print(f"Digite os elementos da matriz {n}x{n}:")
    for i in range(n):
        linha = []
        for j in range(n):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    simetrica = all(matriz[i][j] == matriz[j][i] for i in range(n) for j in range(n))
    if simetrica:
        print("A matriz É simétrica.")
    else:
        print("A matriz NÃO é simétrica.")

elif code == 13:
    matriz = []
    print("Digite os 25 elementos da matriz 5x5:")
    for i in range(5):
        linha = []
        for j in range(5):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    print("Elementos da diagonal secundária:")
    for i in range(5):
        print(f"  [{i}][{4-i}] = {matriz[i][4-i]}")

elif code == 14:
    m = int(input("Linhas de A: "))
    k = int(input("Colunas de A / Linhas de B: "))
    n = int(input("Colunas de B: "))
    A = []
    print(f"Digite os elementos da matriz A ({m}x{k}):")
    for i in range(m):
        linha = []
        for j in range(k):
            val = int(input(f"  A[{i}][{j}]: "))
            linha.append(val)
        A.append(linha)
    B = []
    print(f"Digite os elementos da matriz B ({k}x{n}):")
    for i in range(k):
        linha = []
        for j in range(n):
            val = int(input(f"  B[{i}][{j}]: "))
            linha.append(val)
        B.append(linha)
    C = [[sum(A[i][p] * B[p][j] for p in range(k)) for j in range(n)] for i in range(m)]
    print(f"Resultado da multiplicação A x B ({m}x{n}):")
    for linha in C:
        print(linha)

elif code == 15:
    n = int(input("Ordem da matriz quadrada (n): "))
    matriz = []
    print(f"Digite os elementos da matriz {n}x{n}:")
    for i in range(n):
        linha = []
        for j in range(n):
            val = int(input(f"  [{i}][{j}]: "))
            linha.append(val)
        matriz.append(linha)
    rotacionada = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotacionada[j][n - 1 - i] = matriz[i][j]
    print("Matriz rotacionada 90° (sentido horário):")
    for linha in rotacionada:
        print(linha)

else:
    print("Type a valid exercise")
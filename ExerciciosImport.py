import math
code = int(input("choose your exercise (1-4)\n"))

if code == 1:
    print(math.sqrt(49))

elif code == 2:
    import FuncoesExerciciosImport

    FuncoesExerciciosImport.saudacao()

elif code == 3:
    print("A diferença entre 'import modulo' e 'from modulo import funcao' é que o primeiro importa todo o modulo com todas as suas funcoes, etc. e o"
          " segundo importa apenas uma funcao, classe ou variavel expecifica ")

elif code == 4:
    print("Quando você escreve import math, o Python procura primeiro por um arquivo chamado math.py no diretório atual."
            " se esse arquivo existir, ele será carregado em vez do módulo interno da biblioteca padrão e impossobilitara o uso dela.")
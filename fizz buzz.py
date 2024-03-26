def fizzbuzz(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("fizzbuzz")
        elif num % 3 == 0:
            print("fizz")
        elif num % 5 == 0:
            print("buzz")
        else:
            print(num)

inicio = int(input("digite o numero inicial do intervalo: "))
fim = int(input("digite o numero final do intervalo: "))

fizzbuzz(inicio, fim)

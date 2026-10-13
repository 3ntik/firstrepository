a = int(input("Введите число для поиска делителей: "))
def delit(a):
    mn = []
    for i in range(1, int(a ** 0.5) + 1):
        if (a % i == 0) and (i != int(a ** 0.5)): #добавлено ветвление для проверки 
            mn.append(i)
            mn.append(a//i)
        elif (a % i == 0) and (i == int(a ** 0.5)):
            mn.append(i)
    return mn
print(f"Делители вашего числа: {delit(a)}")

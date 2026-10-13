a = int(input("Введите вичло для поиска делителей: "))
def delit(a):
    mn = []
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            mn.append(i)
            mn.append(a//i)
    return mn
print(f"Делители вашего числа: {delit(a)}")

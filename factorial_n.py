n = int(input("Введіть число n: "))

product = 1

for product_n in range(1, n + 1):
    product *= product_n
print("Факторіал числа n = ", product)

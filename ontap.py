n = int(input("Nhập cạnh của hình tam giác vuông: "))
if n>0:
    for i in range(1, n+1):
        print("*"*i)
else:
    raise Exception(f"Cạnh của tam giác không thể là {n}!")
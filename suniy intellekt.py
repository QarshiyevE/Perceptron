n = int(input("Butun son kiriting (n)= "))

# Thresholdni olish uchun sikl
while True:
    threshold = float(input("Threshold= "))
    if threshold < n and threshold > 0:
        break
    else:
        print(f"Threshold 0 dan {n} gacha bolishi kerak.")

xn = []
wn = []

# 0 yoki 1 ni kiriting
print("0 yoki 1 ni kiriting")
for i in range(n):
    while True:
        k = float(input(f"x{i + 1} = "))
        if k == 0 or k == 1:
            xn.append(k)
            break
        else:
            print("0 yoki 1 ni kiriting.")

# 0 dan 1 gacha kiriting
print("0 dan 1 gacha kiriting")
for i in range(n):
    while True:
        k = float(input(f"w{i + 1} = "))
        if 0 < k < 1:
            wn.append(k)
            break
        else:
            print("0 dan 1 gacha kiriting.")

# Summani hisoblash
sum_result = sum(xn[i] * wn[i] for i in range(n))

# Natijani chiqarish
if sum_result > threshold:
    print(f"Sum: {sum_result}")
    print(True)
else:
    print(f"Sum: {sum_result}")
    print(False)
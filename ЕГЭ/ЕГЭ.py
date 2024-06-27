#Текстовый файл состоит из символов T, U, V, W, X, Y и Z.
#Определите в прилагаемом файле максимальное количество идущих подряд символов (длину непрерывной подпоследовательности),
#среди которых символ Х встречается не более 140 раз.

try:
    with open('313_24.txt', 'r') as f:
        s = f.read()
except FileNotFoundError:
    print("Файл не найден.")
    exit()
except IOError:
    print("Ошибка при чтении файла.")
    exit()

if not s:
    print("Файл пустой.")
    exit()

t = 140
a = s.split('X')
k = 0
kmax = 0

for j in range(0, t+1):
    k = k + len(a[j])
    if j != t:
        k = k + 1

for i in range(t+1, len(a)):
    kmax = max(kmax, k)
    k = k - len(a[i-t-1])
    k = k - 1
    k = k + 1
    k = k + len(a[i])

kmax = max(kmax, k)

print(kmax)
# Задача: Дан размер файда в байтах.Используя операцию деления нацело, найти количество полных килобайтов, которые
# занимает данный файл (1 килобайт = 1024 байта)
try:
   K = int(input("Введите число в килобайтах (минимум 1024:)"))
   B = 1024
   V = K // B
   if K >= 0:
       print(V, "Полных Килобайтов")
   else:
       print("Отрицательное число")
except:
    print("Введите другое число")

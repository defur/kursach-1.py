import random
import time

class Massiv(object):
    def __init__(self, mas, num, k):
        self.mas = mas
        self.k = k
        for i in range(num):
            mas.append(round(random.uniform(-10.009, 10.009), 3))

    def First(self):
        s = 0
        w = 1
        for i in range(len(mas)):
            if (i + 1) % 2 == 0:
                if mas[i] > 0:
                    s += mas[i]
        w = w + 1
        return s

    def Second(self, k):
        while k > len(self.mas):
            print("Количество чисел превышает количество елементов массива")
            k = int(input("Ведите количество чисел:"))
        print(f'До:    {self.mas}')
        k = len(mas) - k
        for_sort = self.mas[k:]
        self.mas = self.mas[:k]
        for_sort.sort(reverse=True)
        done = self.mas + for_sort
        self.mas = done
        print(f'После: {done}')


num = int(input("Введите размер массива: "))
mas = []
k = int(input("Ведите количество чисел:"))

start_time = time.time()

viv = Massiv(mas, num, k)

print(f"Сгенерированный массив: {mas}")

qwe = viv.First()
print(f"Сумма индексов {qwe}")

viv.Second(k)

print("Время выполнения программы:%s" % (time.time() - start_time))

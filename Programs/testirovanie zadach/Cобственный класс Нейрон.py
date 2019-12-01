
# Реализуйте класс "Нейрон", у которого будет несколько методов:
#
#  __init__. Принимает на вход массив весов нейрона --- w=(w1,…,wn), а также функцию активации f (аргумент по умолчанию f(x)=x). Сохраняет веса и функцию внутри класса.
# forward. Принимает на вход массив x=(x1,…,xN) --- входы нейрона. Возвращает f(w1x1+…+wnxn).
# backlog. Возвращает массив x, который подавался на вход функции forward при её последнем вызове.

class Neuron:

    def __init__(self, w, f=lambda x: x):
        self.w = w
        self.f = f

    def forward(self, x):
        self.x = x
        sum = 0
        for i in range(len(x)):
            sum = sum + self.w[i] * x[i]
        return self.f(sum)

    def backlog(self):
        return self.x

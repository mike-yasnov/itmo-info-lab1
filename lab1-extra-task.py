class Converter:
    def __init__(self, n: int) -> None:
        """
        n - колиечство разрядов числа фиббоначи
        """

        self.n = n
        self.__fibbonachi_series = list(self.__fib(n))[1:]
        self.__maxn = sum([9*x for x in self.__fibbonachi_series])


    def __fib(self, n) -> int:
        """
        Генератор чисел фибоначчи 
        n - количсетво чисел на выход 
        """

        a, b = 1, 1
        for _ in range(n+1):
            yield a
            a, b = b, a + b


    def tenth2fib(self, number: int) -> str:
        """
        Перевод из десятичной СС в СС Фибоначчи
        number - число в десятичной системе счисления.
        """

        result = [0]*self.n
        i = self.n - 1
        if self.__maxn > number:
            while number > 0:
                if number - self.__fibbonachi_series[i] >= 0:
                    number -= self.__fibbonachi_series[i]
                    result[i] += 1
                else:
                    i -= 1

            result = ''.join([str(x) for x in result[::-1]])
            result = result[result.find('1'):]
                
            return result
        else:
            raise ValueError('Недостаточное число разрядов для введенного числа.\n\
Пожалуйста, объявите класс Converter с большим количеством разрядов')
        

if __name__ == '__main__':
    converter = Converter(10)
    n = int(input('Введите число в десятичной системе счисления: '))
    print(f'Число {n} в сс Фибоначчи: {converter.tenth2fib(n)}')

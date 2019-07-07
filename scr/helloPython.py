#!/usr/bin/python3

class pythonLearn1:
    print("Hello,python")

    words = ['cat', 'window', 'defenestrate']
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)

    print(words)

    for x in range(-10, -100, 30):
        print(x)

    def fib(n):  # return Fibonacci series up to n
        result = []
        a, b = 0, 1
        while a < n:
            result.append(a)  # see below
            a, b = b, a + b
        return result

    # 调用函数,输出 斐波那契数列
    print(fib(1000))

    def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise OSError('uncooperative user')
            print(complaint)

    ask_ok("是否允许?[y/n]:")

    def f(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L

    print(f(1))
    print(f(2))
    print(f(3))


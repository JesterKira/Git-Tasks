import sys


class Test:

    def calculate(myCondition: str) -> None:

        resCondition = []
        n = 0

        for i in range(len(myCondition)):
            if myCondition[i] in ('+', '-', '*', '/', '^'):
                resCondition.append(myCondition[n:i])
                resCondition.append(myCondition[i])
                n = i + 1
        resCondition.append(myCondition[n:])

        def remover(i, result):
            resCondition.remove(resCondition[resCondition.index(
                i)-1])
            resCondition.remove(resCondition[resCondition.index(
                i)+1])
            resCondition.insert(resCondition.index(
                i)+1, result)
            resCondition.remove(resCondition[resCondition.index(
                i)])

        def multiply():
            for i in resCondition:
                if i == '*':
                    result = float(resCondition[resCondition.index(
                        i)-1]) * float(resCondition[resCondition.index(i)+1])
                    remover(i, result)
                    multiply()

        def division():
            for i in resCondition:
                if i == '/':
                    result = float(resCondition[resCondition.index(
                        i)-1]) / float(resCondition[resCondition.index(i)+1])
                    remover(i, result)
                    division()

        def exponentiation():
            for i in resCondition:
                if i == '^':
                    result = float(resCondition[resCondition.index(
                        i)-1]) ** float(resCondition[resCondition.index(i)+1])
                    remover(i, result)
                    exponentiation()

        def subtraction():
            for i in resCondition:
                if i == '-':
                    result = float(resCondition[resCondition.index(
                        i)-1]) - float(resCondition[resCondition.index(i)+1])
                    remover(i, result)
                    subtraction()

        def summary():
            for i in resCondition:
                if i == '+':
                    result = float(resCondition[resCondition.index(
                        i)-1]) + float(resCondition[resCondition.index(i)+1])
                    remover(i, result)
                    summary()

        exponentiation()
        division()
        multiply()
        subtraction()
        summary()

        return print(float(resCondition[0]))

    def myPrint(string: str) -> None:
        return print(string)


def checkStartParams():
    if len(sys.argv) > 1:
        if sys.argv[1] == Test.calculate.__name__:
            Test.calculate(sys.argv[2])
        if sys.argv[1] == Test.myPrint.__name__:
            Test.myPrint(sys.argv[2])
    else:
        chooseFunc = input('').replace(' ', '').split('(', maxsplit=1)
        condition = str(chooseFunc[1]).replace('(', '').replace(')', '')

        print(chooseFunc)
        print(condition)

        if hasattr(Test, chooseFunc[0]):
            if chooseFunc[0] == Test.calculate.__name__:
                Test.calculate(condition)
                print('True')
            if chooseFunc[0] == Test.myPrint.__name__:
                Test.myPrint(condition)
                print('True')
        else:
            print('False')


checkStartParams()

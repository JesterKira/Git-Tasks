import sys


class MethodsHolder:
    parts = []

    def calculate(conditionString: str) -> None:

        lastPartLeftPosition = 0

        for i in range(len(conditionString)):
            if conditionString[i] in ('+', '-', '*', '/', '^'):
                MethodsHolder.parts.append(
                    conditionString[lastPartLeftPosition:i])
                MethodsHolder.parts.append(conditionString[i])
                lastPartLeftPosition = i + 1
        MethodsHolder.parts.append(conditionString[lastPartLeftPosition:])

        MethodsHolder.__calculateOperator__(
            '/', lambda x, y: float(x)/float(y))
        MethodsHolder.__calculateOperator__(
            '*', lambda x, y: float(x)*float(y))
        MethodsHolder.__calculateOperator__(
            '-', lambda x, y: float(x)-float(y))
        MethodsHolder.__calculateOperator__(
            '+', lambda x, y: float(x)+float(y))

        return print(float(MethodsHolder.parts[0]))

    def __remover__(i, result):
        MethodsHolder.parts[i] = result
        MethodsHolder.parts.pop(i+1)
        MethodsHolder.parts.pop(i-1)

    def __calculateOperator__(operator, func) -> None:
        i = 0

        while i < len(MethodsHolder.parts):
            if MethodsHolder.parts[i] == operator:
                result = func(
                    MethodsHolder.parts[i-1], MethodsHolder.parts[i+1])
                MethodsHolder.__remover__(i, result)
                MethodsHolder.__calculateOperator__(operator, func)
            i += 1

    def myPrint(string: str) -> None:
        return print(string)


def checkStartParams():
    if len(sys.argv) > 1:
        if sys.argv[1] == MethodsHolder.calculate.__name__:
            MethodsHolder.calculate(sys.argv[2])
        if sys.argv[1] == MethodsHolder.myPrint.__name__:
            MethodsHolder.myPrint(sys.argv[2])
    else:
        chooseFunc = input('').replace(' ', '').split('(', maxsplit=1)
        condition = str(chooseFunc[1]).replace('(', '').replace(')', '')

        if hasattr(MethodsHolder, chooseFunc[0]):
            if chooseFunc[0] == MethodsHolder.calculate.__name__:
                MethodsHolder.calculate(condition)
            if chooseFunc[0] == MethodsHolder.myPrint.__name__:
                MethodsHolder.myPrint(condition)
        else:
            print('False')


checkStartParams()

fibonacciArr, count, fibonacciNumber = [0, 1, 1], 0, int(input())
def fibonacci():
    global fibonacciArr, count, fibonacciNumber
    x = (len(fibonacciArr)) - 1
    fibonacciArr.append(fibonacciArr[x] + fibonacciArr[x-1])
    if count < fibonacciNumber:
        count += 1
        fibonacci()
    else:
        return fibonacciArr[(len(fibonacciArr)) - 1]
fibonacci()
print(fibonacciArr[(len(fibonacciArr)) - 1])
def f(x):
    if type(x) != float:
        return x
    return (0-x)
x = int(input())
print(f(x))
def powers(x):
    sum = x**2
    return sum

print(powers(int(input('Pick a number?\n'))))

def stringOutput(word):
    print(word)

stringOutput('Last chance')


def multipram(x,y,z,a=5,b=2):
    """"
    well this is fun
    just let it end
    """
    print(x,y,z,a,b)

multipram(1,2,3)
multipram(1,2,3,8,7)

def divTwo(x):
    return x / 2

def multiFour(x):
    return x * 4
x=10
y=divTwo(10)
print(multiFour(y))

print(divTwo(multiFour(int(input('Pick a number? \n')))))

def casting(x):
    try:
        print(float(x))
    except ValueError:
        print('Please pick a number')
        
casting(input('Enter a number?\n'))
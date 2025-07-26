
numero =1
while numero<=100:
    if numero % 5==0 and numero%7 == 0:
        print(f"{numero} FizzBuzz")
    elif numero %7 ==0:
        print(f"{numero} Buzz")
    elif numero % 5 ==0:
        print(f"{numero} Fizz")
    else:
        print(numero)
    numero +=1
N = int(input())

if N % 3 == 0:
    if N % 5 ==0:
        print("Fizz Buzz")
    else:
        print("Fizz")
    
elif N % 5 == 0:
    print("Buzz")
    
else:
    print(N)
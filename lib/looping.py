def happy_new_year():
     # write your code here
    countdown =10
    while countdown in range(10,0,-1):
     print(countdown)
    countdown -=1
print("Happy New Year!")

    


def square_integers(int_list):
     # write your code here
     return [i ** 2 for i in int_list]

    

def fizzbuzz():
    # write your code here
    for i in range(1,101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
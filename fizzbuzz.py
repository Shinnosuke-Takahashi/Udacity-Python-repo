# This program prints numbers 1 to 100, but with the following conditions:
# 1) If the number is divisible by 3, the program will print "Fizz" instead of the number.
# 2) If the number is divisible by 5, the program will print "Buzz" instead of the number.
# 3) If the number is divisible by 3 and 5, the program will print "FizzBuzz" instead of the number.

def fizzbuzz():
    i=1
    while i<=100:
        if i%3==0 and i%5==0:
            print "FizzBuzz"
        elif i%3==0:
            print "Fizz"
        elif i%5==0:
            print "Buzz"
        else:
            print i
        i=i+1

fizzbuzz()

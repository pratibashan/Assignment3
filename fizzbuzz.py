
number = int(input("Enter a number: "))

if (number % 3 == 0 and number % 5 == 0):    
    print("FIZZ BUZZ") 
elif (number % 5 == 0):
    print("BUZZ")

elif (number % 3 == 0):
    print("FIZZ")


else:
    print("Number is not divisible by both 3 and 5")
       


import calculator

first_number = float(input("Enter the first number: "))
operand  = input("Enter the operand: ")
second_number = float(input("Enter the second number: "))

answer = 0

if operand == "+" :
    answer = calculator.add(first_number,second_number)
    #answer = format(answer,".2f")
    #print (f"The answer is {answer}")

elif operand == "-" :
    answer = calculator.subtract(first_number,second_number) 
    #print (f"The answer is {answer}")

elif operand == "*" :
    answer = calculator.multiply(first_number,second_number)    
    #print (f"The answer is {answer}")

elif operand == "/" :
    answer = calculator.divide(first_number,second_number) 
    #print (f"The answer is {answer}") 

else:
    print("Enter a valid number")   

answer = format(answer,".2f")
print (f"The answer is {answer}")


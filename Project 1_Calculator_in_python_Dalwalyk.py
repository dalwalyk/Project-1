print("select an operation to conduct:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLICATION")
print("4. DIVIDE")

operation = input()
## This method is for addition

if operation == "1":
    num1 = input("Enter first digit: ") 
    num2 = input("Enter second digit: ")
    print("The total is " + str(int(num1) + int(num2)))

## This method is for subtraction
    
elif operation == "2":
    num1 = input("Enter First digit: ") 
    num2 = input("Enter second digit: ")
    print("The total is " + str(int(num1) - int(num2)))

## This method is for multiplication
    
elif operation == "3":
    num1 = input("Enter First digit: ") 
    num2 = input("Enter second digit: ")
    print("The total is " + str(int(num1) * int(num2)))
    
## This method is for division
    
elif operation == "4":
    num1 = input("Enter First digit: ") 
    num2 = input("Enter second digit: ")
    print("The total is " + str(int(num1) / int(num2)))
else:
    print ("Invalid Input")


##Name: Yashi Dalwala
##Assignment: Project_1
##Date: 27/02/2023    
##Work Cited:
https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3
    



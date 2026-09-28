print("===Welcome to Danfoldio's mini calculator===")
num1= float(input("Enter your first number"))
op= input("Choose your operation (+, -,*,/): ").strip()
num2= float(input("Enter your second number:"))
if op=="+":
    Result= num1 + num2
elif op=="-":
    Result= num1 - num2
elif op=="*":
    Result= num1 * num2
elif op=="/":
    if num2!=0:
        Result= num1 / num2
    else:
        Result="Error, cannot divide by Zero"
else:
    Result= "Invalid operator"
print(f"Your answer is:", {Result})
    

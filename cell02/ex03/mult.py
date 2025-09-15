no1 = int(input("number1 : "))
no2 = int(input("number2 : "))

x = no1*no2
print(f"{no1} x {no2} = {x}")

if x > 0 :
    print("The result is positive.")
elif x < 0 :
    print("The result is negative.")
else: print("The result is positive and negative.")
num1 = int(input("Enter the 1st number:"))
num2 = int(input("Enter the 2nd number:"))
print(f"Numbers are {num1} and {num2}")
print("\n\n")

if num1 > num2:
    print(f"{num1} is greater")
elif num1 < num2:
    print(f"{num2} is greater")
else:
    print(f"{num1} and {num2} are equal")

print("++++++++++++++++END++++++++++++++++")
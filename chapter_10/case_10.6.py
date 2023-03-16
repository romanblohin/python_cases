print("Give me two numbers, and I'll give you a sum of them.")

first_number = input("\nFirst number: ")
second_number = input("Second number: ")
try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please enter a number")
else:
    print(answer)

try:
    number = int(input("Enter a number: "))
    result = 10/ number

# if try error, it will execute except
except ValueError:
    print("Invalid input!!! Try number")

except ZeroDivisionError:
    print("Invalid input!!! Cannot divide by zero")

except Exception as error:
    print(f"Error: {error}")

# if try is not error, it will execute else
else:
    print(f"The result is: {result}.")

print("---------------Ending----------------")
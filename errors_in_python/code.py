# catching errors
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grades = []
# this will raise an error if we have no grades:
# average = divide(sum(grades),len(grades))
# print(f"The average grades were {average}")

# this will catch our error
try:
    average = divide(sum(grades),len(grades))
except ZeroDivisionError:
    print("No Average grades were found")
else:
    print(f"The average grades were {average}")
# Types of errors
# TypeError
# ValueError
# RuntimeError
# ZeroDivisionError
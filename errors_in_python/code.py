# catching errors
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

grades = [23, "a"]
# this will raise an error if we have no grades:
# average = divide(sum(grades),len(grades))
# print(f"The average grades were {average}")

# this will catch our error
try:
    # try our average function to create the average variable
    average = divide(sum(grades),len(grades))
# catch if we have no grades and we raise an error in our divide function
except ZeroDivisionError:
    print("No Average grades were found")
# catch if the grades array has non integer value
except TypeError:
    print("Only numbers are allowed")
# add an else to happen if successful
else:
    print(f"The average grades were {average}")
finally:
# add a finally to go off regardless of the outcome at the end
    print("Thanks for Computing!")
# Types of errors
# TypeError
# ValueError
# RuntimeError
# ZeroDivisionError
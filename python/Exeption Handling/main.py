a = int(input("tell your number:-"))

try:
    print(10/a)

except ZeroDivisionError:
    print("You cannot divide by zero, please enter a non-zero number."  )

else:
    print("there is no error")

finally:
    print('Always run no matter what')

print("This line will always execute after the try-except block.")

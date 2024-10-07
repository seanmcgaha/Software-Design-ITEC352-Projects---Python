def calculator(a, b, operation): #Parenthesis added

  if operation == 'add':

    return a + b

  elif operation == 'subtract':

    return a - b

  elif operation == 'multiply':

    return a * b

  elif operation == 'divide':

    if b != 0:

      return a / b

    else:

      return "Error: Division by zero"

  else:

    return "Invalid operation" #added second quotation mark



# Example usage

result = calculator(10, 5, 'add')

print("Result:", result)


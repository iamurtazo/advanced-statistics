def sum(a, b):
  return a + b

ali = sum(4, 8)
print(ali)


def is_armstrong(a: int):
  # convert the number to a string to iterate through its digits
  str_a = str(a)
  # get the number of digits in the number
  num_digits = len(str_a)
  # initialize a variable to hold the sum of the digits raised to the power of the number of digits
  armstrong_sum = 0
  # iterate through each digit in the number
  for digit in str_a:
    # convert the digit back to an integer and raise it to the power of the number of digits, then add it to the armstrong_sum
    armstrong_sum += int(digit) ** num_digits
  # check if the armstrong_sum is equal to the original number
  if armstrong_sum ==a: 
    return f'yes {a} is an armstrong number'
  else:
    return f'no {a} is not an armstrong number'

print(is_armstrong(153))

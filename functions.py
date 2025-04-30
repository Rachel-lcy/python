# create a function
# def print_5_times(parameter = 'loop',loop_amount = 5):
#   counter =0
#   # print(global_var)
#   while counter <= loop_amount:
#     print(counter,parameter)
#     counter += 1
#   return 'something else'

# def hypotenuse_calculator(side_a, side_b):
#   hypotenuse = (pow(side_a, 2) + pow(side_b, 2)) ** 0.5
#   return round(hypotenuse,2)

# call
# print('print')
# global_var = 'global variable'
# test = print_5_times('something', 4)
# print(test)
# print(hypotenuse_calculator(5,4))


# exercise
def shouter (output_string ='Hello', repetition_amount = 2):
  # print(list(range(repetition_amount)))

  if repetition_amount <= 10:
    for i in range(repetition_amount):
      print(output_string.upper())
  else:
    print('You are too loud')
  return 'Done'

status = shouter()
print(status)







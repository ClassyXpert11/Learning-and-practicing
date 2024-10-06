#This example is taken from moodle notes
def check_even_list(num_list):
  # Go through each number
  for number in num_list:
    # Once we get a "hit" on an even number, we return True
    if number % 2 == 0:
      return True
    # Don't do anything if its not even
    else:
      pass
    # Notice the indentation! This ensures we run through the entire for loop 
  return False

print(check_even_list([1,2,3,4,5,6,7,8,9,10])) 

def check_odd_list(num_list2):
  for odd in num_list2:
    if odd %3==0:
      return True
    else:
      pass
  return False

print(check_odd_list([1,2,3,4,5,6,7,8,9,10]))


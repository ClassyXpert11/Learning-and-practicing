#This is getting the numbers 1 to 100
for number in range(1, 101):
  #This is line of code is saying that if there is a multiple of 3 AND 5 then it should print "FizzBuzz"
  if number%3==0 and number%5==0:
    print(str(number) + " FizzBuzz")
  #This line does the same thing as the previous one but for the multiples of 3 it will print "Fizz"
  elif number %3==0:
    print(str(number) + " Fizz")
  #This line also does the same thing as the previous one but for the multiples of 5 it will print "Buzz"
  elif number %5==0:
    print(str(number) + " Buzz")
  #This line of code just print out the number from 1 to 100
  else:
    print(number)
  


    

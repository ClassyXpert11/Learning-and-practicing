st = "Print every word in this sentence that has an even number of letters"
kj = st.split()
#This code splits the variable "st" into multiple different strings


#This is an attempt to try to print "Even!" whenever a word has an even amount of letters.
for even in kj:
  if len(even)%2==0:
    print("Even!")
    print(even)
  



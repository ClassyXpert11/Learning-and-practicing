#This is the string that we will be using to print out the first letters of each word with.
st = "Create a list of the first letters of every word in this string"
#This variable allows us to split the string into mutiple strings.
stt = st.split()
#This list is where we will be putting the string into. I used the zero indexing here as that is the first letter of each word in the string. I also used the variable "stt" instead of "st" as that is the one that that will allow us to grab the first letter of each word in the string since it has been split.
first_letter_list = [fl[0] for fl in stt]
#This line of code prints out the list which then in turn prints out the final result which is the first letter of each word.
print(first_letter_list)


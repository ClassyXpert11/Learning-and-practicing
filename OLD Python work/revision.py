# Need to get 165.8
import math

numbers = 15**2+10/2*1-64.2
print(numbers)

numbers2 = 0.1+0.2-0.3
round(numbers2, 1)
print(numbers2)

print(math.ceil(1.34))

math.pi*43.5**2

# math.sqrt(9)
# math.trunc(1.23456678990, 5)

print(math.ceil(6.01))
print(math.ceil(7.95))
print(math.ceil(4.53))

print(math.pi*23.6**2)
print(math.pi*12.7**2)
print(math.pi*75.2**2)

print(math.sqrt(16))
print(math.sqrt(25))
print(math.sqrt(36))

print(math.trunc(2.26534))
print(math.trunc(7.2364326234))
print(math.trunc(234.3462152165))

string1 = "Hello World!"
print(string1[6])
"Hello World!"[6]
print(string1[-6])
"Hello World!"[-6]

print(string1[6:11:1])
"Hello World!"[6:11:1]

print(string1[::2])

print(string1[::-1])

# practice string
string2 = "Raspberry and banana"
print(string2[3])
print(string2[-17])

print(string2[0:10:1])

print("Jai Somaiya"[::-1])
print(" ".join("I am Here".split(" ")[::-1]))
print("Hello World".replace(" "," "))
#"Hello"[0]="J"

S = "jai somaiya"
LS = S.split(" ")
ns = LS[0].capitalize()+LS[1].capitalize()

print(S)
print(LS)
print(ns)

js = ["Green", "Blue", "Red", "orange", "Purple", "Pink", "Yellow"]

print("<~>".join(js))


#Exercise 1

a_list = [1, 2, 3, 4, 5, 6, 7]

a_list[0] = a_list[0]**2
a_list[1] = a_list[1]**2
a_list[2] = a_list[2]**2
a_list[3] = a_list[3]**2
a_list[4] = a_list[4]**2
a_list[5] = a_list[5]**2
a_list[6] = a_list[6]**2

print(a_list)


#Exercise 2

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

a = list1[0] +list2[0]

b = list1[0] + list2[1]

c = list1[1] + list2[0]

d = list1[1] + list2[1]

abcd = [a, b, c, d]
print(abcd)

#Exercise 3

aa_list = [100, 200, 300, 400, 500]
print(aa_list[::-1])
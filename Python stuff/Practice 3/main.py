def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num3 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300,40,5))



monthconversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthconversions.get("Jun" , "Not a month dumb cunt"))


num1 = float(input("Enter number = \n"))
op = input("Enter operator = \n")
num2 = float(input("Enter number = \n"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator u dumb fuck")
def converter(cel):
    msg1 = "degree celsius are"
    msg2 = "degree fahrenheit"
    result = (cel * 9/5) + 32
    return str(cel) + " " + msg1 + " " + str(result) + " " + msg2

user_input = input("Enter temperature in Celsius: ")
f_result = converter(float(user_input))
print(f_result)
password = input("Enter new password: ")
result = {}

if len(password) >=8:
    result["length"] =True

else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase=False
for i in password:
    if i.isupper():
        uppercase=True



result["uppercase"] = uppercase

print(result)
print(all(result))

if all(result):  ##== True:
    print("password is very strong")
else:
    print("weak password")
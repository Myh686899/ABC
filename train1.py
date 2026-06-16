""" contacts={"A":"123",
          "B":"456"}
contacts["C"]="789"
del contacts["A"]
print(contacts)
print("D"in contacts) 
print(contacts.keys())
print(contacts.values())
print(contacts.items()) """


""" mark_list = {"A":601,"B":503,"B":559,"C":672,"D":300}
for id,mark in mark_list.items():
    if mark>=600:
        print(id,mark,"good") """


""" for num in range(1,10,2):
    print(num,end=" ") """


message_content = """{year},{name}""".format(year="hu",name="huang")
print(message_content)

hobby = "TV"
message_content2 = f"""{hobby}"""
print(message_content2)


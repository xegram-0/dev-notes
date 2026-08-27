import time

obj = time.localtime()
str_time = time.strftime("%c",obj) # has to have a format before
#print(str_time)
#print(obj)
#new_obj = time.mktime(obj)
#print(new_obj)
#another = time.gmtime(0)
#print(another)


# Walrus operator (:=) kinda like Pascal
# Allow assigning value within a statement
ages = [3,18,56]

if (age := int(input("Enter age: "))) in ages:
    print(f"You are {age}")
else:
    print("Age not found")
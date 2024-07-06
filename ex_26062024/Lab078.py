# Revision without constructor and with constructor

# Lets create class

# class Akashtara():
#     name = None
#     age = None
#
#     # Here no need to craete an attribute, directly we are calling at end
#     def sleep(self):  # behaviour
#         print("sleeping")
#
#     def walk(self):
#         print("sleeping")
#
#     def run(self):
#         print("sleeping")
#
#
# # lets create an object
#
# Member1 = Akashtara()
# print(Member1.name, Member1.age)
# Member1.name = "Pratiksha"
# Member1.age = "25"
# Member1.sleep()
# print(Member1.name, Member1.age, sep=" | ")
#
# Member2 = Akashtara()
# print(Member2.name, Member2.age)
# Member2.name = "Savita"
# Member2.age = "45"
# Member2.walk()
# print(Member2.name, Member2.age, sep=" | ")
#
# Member3 = Akashtara()
# print(Member3.name, Member3.age)
# Member3.name = "Akash"
# Member3.age = "32"
# Member3.run()
# print(Member3.name, Member3.age, sep=" | ")
#
# Member4 = Akashtara()
# print(Member4.name, Member4.age)
# Member4.name = "Vijay"
# Member4.age = "65"
# Member4.sleep()
# print(Member4.name, Member4.age, sep=" | ")



#Now same program will create by constructor

class Akashtara():
    name = None
    age = None

#here will craete an attribute by passing arguments

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sleep(self):  # defining  behaviour
        print("sleeping")

    def walk(self):
        print("sleeping")

    def run(self):
        print("sleeping")

# lets create an object
Member1 = Akashtara("Pratikha","25")
# print(Member1.name, Member1.age, sep=" : ")
print(f'{Member1.name}has age equals to {Member1.age}')#print buy formatting
Member1.sleep()

Member2 = Akashtara("Savita","56")
print(Member2.name, Member2.age, sep=" : ")
Member1.walk()

Member3 = Akashtara("Akash","32")
print(Member3.name, Member3.age, sep=" : ")
Member1.run()

Member4 = Akashtara("Vijay","65")
print(Member4.name, Member4.age, sep=" : ")
Member1.sleep()
# # lets create class, object and function/method
#
# # create object of person class
#
# # object ref =object()
#
class Dog:
    name = None
    id = None

#
# # every class has attribute and behaviour
# # attribute - variable
# # behaviour - method/function
#
    def __init__(self, name, id):  # attributes
        self.name = name
        self.id = id
#
#
    def sleep(self):  # behaviour
        print("who is slepping" + self.name)
#
#
# # Craete object to call
#
dog1 = Dog(name= "Viru",  id= "1")
dog2 = Dog(name= "Chow", id= "2")
# # dog1 = Dog(name= "Viru", id= "1")
# # dog2 = Dog(name="Chow", id= "2")
#
# # print both dog name and id by using formatting
#
print(f'{dog1.name} has id {dog1.id}')
print(f'{dog2.name} has id {dog2.id}')
#
dog1.sleep()
dog2.sleep()
#

#
# class Dog:
#     name = None
#     id = None
#
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def sleep(self):
#         print("Who is Sleeping -> " + self.name)
#
#
# dog1 = Dog("Chow", "1")
# dog2 = Dog("Mow", "2")
#
#
# print(f'{dog1.name} has ID {dog1.id}')
# print(f'{dog2.name} has ID {dog2.id}')
#
# dog1.sleep()
# dog2.sleep()
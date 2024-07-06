#Constructor

#Constructor cannot have return type
#Constructor and Class name should be same in java but in python, constructor called by __init__

 #def default(self):
     #print("default constructor")


class Patients:
    name = None
    blood_grp = None

    def __init__(self, name, blood_grp):
        self.name = name
        self.blood_grp = blood_grp

    def sleep (self):  # behaviours
        print("sleeping")

    def walk (self):
        print("walking")

    def run (self):
        print("running")


patient1 = Patients("Pratiksha", "AB+")   #calling constructor Pratiksha &AB+ as name and blood-grp
print(patient1.name, patient1.blood_grp)
patient1.walk()

print("______________________________________")


#
# patient2 = Patients()
# print(patient2.name)
# patient2.blood_grp = "AB+"
# patient2.name = "Vijay"
# patient2.sleep()
# print(patient2.blood_grp, patient2.name, sep=" | ")
# print("______________________________________")
#
#
# patient3 = Patients()
# print(patient3.name)
# patient3.blood_grp = "A+"
# patient3.name = "Savita"
# patient3.run()
# print(patient3.blood_grp, patient3.name, sep=" | ")
# print("______________________________________")


# Now no need to call this item seperatrly instaede can call in object only which is called as constructor


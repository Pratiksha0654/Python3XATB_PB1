# voting elegibility by labda expression
# age >= 18 > elegible
# age < 18
# not elegible


def voting(age):
    if age >= 18:
        return ("elegible")
    else:
        return ("not elegible")


R1 = voting(20)
print(R1)
#
#
#
R2 = lambda age: "elgible" if age >= 18 else "not elegible"
print(R2(12))

print(lambda age: "elgible" if age >= 18 else "not elegible"(24))

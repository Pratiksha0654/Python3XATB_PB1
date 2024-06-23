# def function with match
# def allowed_to_attend_Python_class (name):
#     match name:
#         case "Pratiksha":
#             print("Pratiksha is allowed to attend the class")
#         case "Akash":
#             print("Akash is allowed to attend the class")
#         case _:
#             print("Not allowed to attend the class")
#
#
# allowed_to_attend_Python_class("Akash")

# ***********************************************

def eligible_for_voting_in_India(age, nationality):
    match (age, nationality):
        case (age, "Indian") if age >= 18:
            print("You are eligible to vote in India")

        case (age, "Indian") if age < 18:
            print("You are not eligible to vote in India")

        case (age, nationality):
            print("You are not eligible to vote in India")


eligible_for_voting_in_India(8, "pakishan")

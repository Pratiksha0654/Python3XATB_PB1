#File IO
import os.path
#
# try:
#     with open("sample.txt","r") as file:
#         print(file.read())
#         file.close()   #FileNotFoundError: [Errno 2] No such file or directory: 'sample.txt'
#     # why we mention file.close ---> to save the python memory
#
#
# except Exception as e:
#    print("I am not able to find the file",e)
#
# finally:
#     print("closing")   #NameError: name 'file' is not defined. Did you mean: 'filter'?


 # how to handle this? use try
try:
        with open("sample.txt", "r") as file:
            print(file.read())
            file.close()

except Exception as e:
        print("I am not able to find the file", e)

finally:
        print("closing")
        try:
         file.close()
        except Exception as ab:
            print(ab)

# I am not able to find the file [Errno 2] No such file or directory: 'sample.txt'
# closing
# name 'file' is not defined


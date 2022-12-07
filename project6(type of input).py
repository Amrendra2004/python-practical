print("Check the type of Input\n")


a = input("Enter any input: ")
if a.isdigit():
    print("The input is in Number.")
elif a.isalpha():
    print("The input is in Letter.")

elif a.isalnum():
    print("The input is in Alpha-Numeric.")
    
else:
    print("The input is in Special Character.")
      
    
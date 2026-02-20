'''
Program Name: String Operations Menu-Driven Program

Description:
This Python program performs multiple operations on a given string
through a menu-driven interface.

It includes...
a) Count Number of Vowel in given string  
b) Count Length of string (do not use Len ())  
c) Reverse string  
d) Find and replace operation  
e) check whether string entered is a palindrome or not 

Author: Hamida Badamdi

'''
# Function to count vowels
def count_vowels(string):
    cnt=0
    for char in string.lower():
        if char in ('a','e','i','o','u'):
            cnt=cnt+1
    print(f"\nTotal no. of vowels in the '{string}' : {cnt}")


# Function to count string length without using len()
def count_str_length(string):
    str_len=0
    for _ in string:
        str_len+=1
    print(f"\nLength of '{string}' is : {str_len}")

# Function to reverse string
def reverse_string(string):
    print(f"\nReverse of '{string}' is : {string[::-1]}")
    
# Function for find and replace    
def find_replace_str(string):
    word=input("Enter word to find : ")
    if  string.find(word) != -1:
        print(f"'{word}' found at position : {string.find(word)}")
    else:
        print(f"'{word}' not found in the '{string}!'")
        return
    new_str=input("Enter new string/word to replace : ")
    string=string.replace(word,new_str)
    print(f"'{word}' is successfully replaced by '{new_str}.'\n=>Updated String : '{string}'")
    
    
# Function to check palindrome
def check_palindrome(string):
    rev_str=""
    for char in range(len(string)-1, -1, -1):
        rev_str+=string[char]

    if string == rev_str:
        print(f"\n=>'{string}' is palindrome string.")
    else:
        print(f"\n=>'{string}' is not palindrome string.")

# Menu-driven function    
def string_opr():
    while True:
        print("\n********String Operations Menu********\n"
              "\n1.Count no. of Vowels"
              "\n2.Count length of string"
              "\n3.Reverse string"
              "\n4.Find and replace operation"
              "\n5.Check palindrome string"
              "\n6.Exit")

        usr_str = input("\nEnter the string value:")
        choice = int(input("\nEnter your choice:"))

        if choice == 1:
            count_vowels(usr_str)
            
        elif choice == 2:
            count_str_length(usr_str)
            
        elif choice == 3:
            reverse_string(usr_str)

        elif choice == 4:
            find_replace_str(usr_str)

        elif choice == 5:
            check_palindrome(usr_str)  
            
        elif choice == 6:
            print("Exiting....")
            break

        else:
            print("Invalid Choice!")

#Calling function....
string_opr()

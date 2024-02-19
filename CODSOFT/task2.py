import random 
import string                   
def password(len): 
    chars= string.ascii_letters + string.digits + string.punctuation    
    s_char = random.sample(chars, len)  
    str = "".join(s_char)  
    return str  

if __name__ == "__main__":  
    while True:   
        user_input = input("Enter y to generate a password and n to exit: ")   
        if user_input == 'n':  
            print("Thank You.")    
            break  
        elif user_input == 'y':   
            len = int(input("Enter the length of the Password: "))  

            pass_str = password(len)  
            print("A randomly generated Password is:", pass_str)  
            print("")    
        else:  
            print("Invalid Input.Try Again.")  
            print("")

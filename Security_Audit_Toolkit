import random
import string
from datetime import datetime

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in "!@#$%^&*" for char in password):
        score += 1
    
    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if score == 5:
        result = "Strong Password"
    elif score >= 3:
        result = "Medium Password"
    else:
        result = "Weak Password"
    return result, score


while True:
    print("\n=== SECURITY AUDIT TOOLKIT ===")
    print("1. Check Password Strength")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        password = input("Enter Password: ")
        result, score = check_password(password)
        current_time = datetime.now()
        file = open("security_report.txt", "a")
        
        file.write("SECURITY AUDIT REPORT\n")
        file.write("---------------------\n")
        file.write("Date & Time: " + str(current_time) + "\n")
        file.write("Password Result: " + result + "\n")
        file.write("Security Score: " + str(score) + "/5\n")
        file.close()

        print("Result:", result)
        print("Security report saved successfully!")

    elif choice == "3":
        print("Goodbye!")
        break

    else: 
        print("Invalid choice")
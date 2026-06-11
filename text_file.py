password = input("Enter Password: ")

result = input("Enter Result (Weak/Medium/Strong): ")

file = open("security_report.txt", "w")

file.write("SECURITY AUDIT REPORT\n")
file.write("---------------------\n")
file.write("Password: " + password + "\n")
file.write("Result: " + result + "\n")

file.close()

print("Report created successfully!")
# Navdeep Kaur
# Python app using if else 
# Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. 
Total_number_of_stds =5
Count_DeanList = 0
Count_Honor =0
for i in range (0,Total_number_of_stds,1 ):
    std_lastname = input("enter the last name of student :")
    if std_lastname =="ZZZ":
        print("enter the details for another student: ")
    else:
        std_firstname =input("enter first name of student :")
        GPA = float(input("enter the GPA of student :"))
        if GPA >=3.5 :
            print("Sudent has made Dean,s list .")
            Count_DeanList = Count_DeanList +1

        elif GPA >=3.25:
            print("student has made the Honor Roll")  
            Count_Honor =Count_Honor +1

print("Total  number od students in Dean's list are: ",Count_DeanList ," and total number of Honor's list are:", Count_Honor) 


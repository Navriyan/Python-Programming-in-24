sec_per_min = int(input("Enter how many seconds are in one minute: "))
min_per_hr = int(input("Enter how many minutes are there in one hour: "))

#number of seconds in an hour
sec_per_hr = sec_per_min * min_per_hr

# Print the number of se60
print("Total number of seconds in one hour is:", sec_per_hr)

# Calculate the number of seconds in a day using the seconds_per_hour variable
hours_per_day = 24
sec_per_day = sec_per_hr * hours_per_day

# Print the number of seconds in a day
print("Total number of seconds in one day is:", sec_per_day)
# calculate for division
result=sec_per_day/sec_per_hr
#  to print result
print("result using floating -point division is :", result) 
# calculation  for integer division
result1= sec_per_day//sec_per_hr
# to print result using integer division
print("result of integer division is :", result1)
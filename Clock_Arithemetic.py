hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

total_minutes = (hour * 60) + mins + duration
end_hour = total_minutes // 60   
end_mins = total_minutes % 60 
final_hour = end_hour % 24  
print()
print("The time is", final_hour, ":", end_mins)

# Test Data

# Sample input:
# 12
# 17
# 59
# Expected output: 13:16

# Sample input:
# 23
# 58
# 642
# Expected output: 10:40

# Sample input:
# 0
# 1
# 2939
# Expected output: 1:0

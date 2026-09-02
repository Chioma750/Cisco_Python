hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

# Write your code here.
total_minutes = (hour * 60) + mins + duration
# total_minutes is now 85 (since 60 + 10 + 15 = 85)
end_hour = total_minutes // 60   # 85 // 60 gives 1 (because 60 goes into 85 once)
end_mins = total_minutes % 60    # 85 % 60 gives 25 (the remainder)
final_hour = 26 % 24  # final_hour becomes 2 (because 26 minus 24 leaves a remainder of 2)

print(final_hour)
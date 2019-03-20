name = input("Please enter your name: ")
print("Hello, " + name)

total_secs = int(input("Please enter the number of seconds you wish to convert: "))
hours = total_secs // 3600
secs_still_remaining = total_secs % 3600
mins = secs_still_remaining // 60
secs_finally_remaining = secs_still_remaining % 60
print("Hrs = ",hours," Mins = ",mins," Secs = ",secs_finally_remaining)

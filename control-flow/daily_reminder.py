"""
Python script that will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.
"""

# user prompt
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ")

# loops
if time_bound == "yes":
    match priority:
        case "high" | "medium" | "low":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
else:
    print(f"{task} is a {priority} priority task. Consider completing it when you have free time.")

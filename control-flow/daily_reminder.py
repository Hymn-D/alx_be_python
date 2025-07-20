task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high"
    message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task. Try to get it done today."
    case "low":
        message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = f"Reminder: '{task}' has an unspecified priority level. Handle as needed."
if time_bound == "yes":
    message += " that requires immediate attention today!"
print(message)
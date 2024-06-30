# Prompt for a single task description
task = input("Enter your task: ")

# Prompt for the task's priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Use Match Case to determine the priority level response
match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be done soon"
    case "low":
        reminder += ". Consider completing it when you have free time"

# Use an if statement to modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " today!"

# Print the customized reminder
print(f"Reminder: {reminder}")

from datetime import date

habits = ["Study", "Exercise", "Meditation", "Reading"]

print("Your habits for today:")
for habit in habits:
    print("-", habit)

completed = []

for habit in habits:
    answer = input(f"Did you complete {habit}? (yes/no): ")
    if answer.lower() == "yes":
        completed.append(habit)

# Display results
print("\nToday's Progress:")
print("You completed:", completed)

# Save results to a log file
today = date.today()
filename = "habit_log.txt"

with open(filename, "a") as file:
    file.write(f"{today} - Completed: {completed}\n")

print("\nProgress saved to habit_log.txt ✅")

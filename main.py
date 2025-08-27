import csv
import os
import matplotlib.pyplot as plt

FILENAME = "tasks.csv"
tasks = []

# --- Load tasks from CSV file ---
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append({"name": row["name"], "done": row["done"] == "True"})

# --- Save tasks to CSV ---
def save_tasks():
    with open(FILENAME, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["name", "done"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for t in tasks:
            writer.writerow({"name": t["name"], "done": t["done"]})

# --- Main functions ---
def add_task(name):
    tasks.append({"name": name, "done": False})
    print(f"Task '{name}' added!")
    save_tasks()

def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nAll tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['name']} [{status}]")

def mark_task_done(number):
    if 0 < number <= len(tasks):
        tasks[number-1]["done"] = True
        print(f"Task '{tasks[number-1]['name']}' marked as done.")
        save_tasks()
    else:
        print("Invalid task number.")

def delete_task(number):
    if 0 < number <= len(tasks):
        print(f"Task '{tasks[number-1]['name']}' deleted.")
        del tasks[number-1]
        save_tasks()
    else:
        print("Invalid task number.")

# --- Visualization ---
def visualize_progress():
    done_count = sum(t["done"] for t in tasks)
    not_done_count = len(tasks) - done_count

    if len(tasks) == 0:
        print("No tasks to visualize.")
        return

    plt.bar(["Done", "Not Done"], [done_count, not_done_count], color=["green", "red"])
    plt.title("Task Progress")
    plt.ylabel("Number of Tasks")
    plt.show()

# --- Menu ---
def menu():
    load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")
        print("6. View task progress")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter task: ")
            add_task(name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            number = int(input("Enter task number: "))
            mark_task_done(number)
        elif choice == "4":
            number = int(input("Enter task number: "))
            delete_task(number)
        elif choice == "5":
            print("Goodbye!")
            break
        elif choice == "6":
            visualize_progress()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()

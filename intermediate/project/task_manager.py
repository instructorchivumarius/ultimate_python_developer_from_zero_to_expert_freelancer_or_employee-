# (1) Creating the CLI Interface
#     A simple command-line menu for our Task Manager project
# (2) Saving Data to JSON File
#     Extending the CLI with JSON data saving
# ___________________________________________________________


# ▼ (2-1) Import Modules for Saving Task Data ▼
import json
# ▼ (2-2) Ensure JSON is saved next to this script (not IDE working dir) ▼
from pathlib import Path


# ▼ (2-3) “Tasks” List (In-Memory)
#                       ► Stores all tasks while the program runs
#                       ► “tasks.json” will be created automatically when saving ▼
tasks = []

# ▼ (2-4) Data File Path (Always Next to this Script) ▼
DATA_FILE = Path(__file__).with_name("tasks.json")



# ▬ (1-1) “Show_Menu()” Function ▬
def show_menu():
    """Display the main menu options"""
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")



# ▬ (2-5) “Save_Tasks()” Function ▬
#            ► Creates "tasks.json" automatically if it does not exist
#            ► Overwrites the file each time with the updated task list
#            ► Saves the file NEXT TO THIS SCRIPT (using pathlib)
def save_tasks():
    """Write the current tasks list to tasks.json (next to this script)"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
    print("Tasks saved successfully!")



# ▬ (1-2) “Main()” Function ▬
def main():
    """Main Program Loop that Runs Until User Exits (updated to save tasks)"""
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Viewing tasks... (to be implemented)")
        elif choice == "2":
            # ▼ (2-6) Add a task and save it to JSON ▼
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)   # (2-3) add to in-memory list
                save_tasks()         # (2-5) persist immediately
                # print(f"Saved to: {DATA_FILE.resolve()}")  # optional debug
            else:
                print("Empty task discarded.")
        elif choice == "3":
            print("Editing a task... (to be implemented)")
        elif choice == "4":
            print("Deleting a task... (to be implemented)")
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")



# ▬ (1-3) “MAIN()” BLOCK ▬
if __name__ == "__main__":
    main()

# (1) Creating the CLI Interface
#     A simple command-line menu for our Task Manager project
# (2) Saving Data to JSON File
#     Extending the CLI with JSON data saving
# (3) Loading and Viewing Tasks
#     Allowing the user to load and display tasks
# ___________________________________________________________



# ▼ (2-1) Import Modules for Saving Task Data ▼
import json
# ▼ (2-2) Ensure JSON is saved next to this script (not IDE working dir) ▼
from pathlib import Path


# ▼ (2-3) “Tasks” List (In-Memory)
#           ► Stores all tasks while the program runs
#           ► “tasks.json” will be created automatically when saving ▼
tasks = []

# ▼ (2-4) Data File Path (Always Next to this Script) ▼
DATA_FILE = Path(__file__).with_name("tasks.json")



# ▬ (1-1) “SHOW MENU()” FUNCTION ▬
def show_menu():
    """Display the main menu options"""
    print("\n--- Task Manager ---")
    # (3-1) We modify the display to clarify "All / Filter"
    print("1. View Tasks (All / Filter)") 
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



# ▬ (3-2) “Load_Tasks()” Function ▬
#            ► Reads existing tasks from tasks.json
#            ► If file does not exist → start with empty list
def load_tasks():
    """Load tasks from tasks.json (if it exists)"""
    global tasks
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []



# ▬ (3-3) “List_Tasks()” Function ▬
#            ► Displays all tasks, with numbering
def list_tasks():
    """Display all tasks in a numbered list"""
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")



# ▬ (3-4) “List_Tasks_Filtered()” Function ▬
#                      ► Displays only tasks that contain the search term
def list_tasks_filtered(term):
    """Display tasks containing the search term"""
    filtered = [t for t in tasks if term.lower() in t.lower()]
    if not filtered:
        print(f'No tasks found containing: "{term}"')
    else:
        print(f'\nTasks containing "{term}":')
        for i, task in enumerate(filtered, start=1):
            print(f"{i}. {task}")



# ▬ (1-2) “MAIN()” FUNCTION → WITH LOOP ▬
def main():
    """Main program loop that runs until user exits"""
    
    # (3-5) Load tasks at startup
    load_tasks()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
             # (3-6) Ask user: show all tasks or filter by keyword
            term = input("Enter search term (leave empty to view all): ").strip()
            if term:
                list_tasks_filtered(term)
            else:
                list_tasks() 
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



# ▬ (1-3) “MAIN()” FUNCTION → INTO “MAIN” BLOCK ▬
if __name__ == "__main__":
    main()

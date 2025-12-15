# (1) Creating the CLI Interface
#     A simple command-line menu for our Task Manager project
# (2) Saving Data to JSON File
#     Extending the CLI with JSON data saving
# (3) Loading and Viewing Tasks
#     Allowing the user to load and display tasks
# (4) Editing and Deleting Tasks
#     Modify or remove tasks and persist the changes
# (5) Safe Exit & Auto-Save Before Closing
#     Confirm exit and always save before quitting
# ___________________________________________________________



# ▼ (2-1) Import Modules for Saving Task Data ▼
import json
# ▼ (2-2) Ensure JSON is saved next to this script (not IDE working dir) ▼
from pathlib import Path
# ▼ (5-3) Import error class for safe JSON loading (handles empty/corrupted files) ▼
from json import JSONDecodeError


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
    # (5-1) Update Exit label to communicate auto-save behavior
    print("5. Exit (Save & Quit)") 



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
        # (5-4) Harden loading: handle empty/corrupted JSON and validate structure
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    tasks = data
                else:
                    print("Warning: tasks.json has unexpected format. Starting with empty list.")
                    tasks = []
        except JSONDecodeError:
            print("Warning: tasks.json is empty or corrupted. Starting with empty list.")
            tasks = [] 
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



# ▬ (4-1) Helper: “Select_Task_Index()” 
#           ► Shows the list, asks for a 1-based index, validates input
#           ► Returns a 0-based index or None if cancelled/invalid ▬
def select_task_index(action_label: str) -> int | None:
    """Show tasks and ask user to choose by number; return 0-based index or None"""
    if not tasks:
        print("No tasks to select.")
        return None

    list_tasks()
    raw = input(f"Enter the task number to {action_label} (or press Enter to cancel): ").strip()
    if not raw:
        print("Cancelled.")
        return None

    if not raw.isdigit():
        print("Invalid input. Please enter a number.")
        return None

    idx_1_based = int(raw)
    if not (1 <= idx_1_based <= len(tasks)):
        print(f"Out of range. Please choose between 1 and {len(tasks)}.")
        return None

    return idx_1_based - 1



# ▬ (4-2) “Edit_Task()” Function 
#           ► Lets the user change the text of a chosen task
#           ► Persists the change to JSON using save_tasks() ▬
def edit_task():
    """Edit an existing task, then save"""
    idx = select_task_index("edit")
    if idx is None:
        return

    old = tasks[idx]
    print(f"Current task: {old}")
    new_text = input("Enter the new text (leave empty to keep unchanged): ").strip()
    if not new_text:
        print("No changes made.")
        return

    tasks[idx] = new_text
    save_tasks()
    print(f"Task #{idx + 1} updated.")



# ▬ (4-3) “Delete_Task()” Function 
#           ► Confirms and removes a chosen task
#           ► Persists the change to JSON using save_tasks() ▬
def delete_task():
    """Delete an existing task after confirmation, then save"""
    idx = select_task_index("delete")
    if idx is None:
        return

    to_delete = tasks[idx]
    confirm = input(f'Confirm delete "{to_delete}"? (y/N): ').strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        return

    removed = tasks.pop(idx)
    save_tasks()
    print(f'Deleted: "{removed}"')



# ▬ (5-2) “Confirm_Exit()” Function ▬
#           ► Ask user to confirm exit
#           ► Auto-save all tasks before quitting
def confirm_exit() -> bool:
    """Confirm exit and save before quitting"""
    confirm = input("Are you sure you want to exit? (y/N): ").strip().lower()
    if confirm == "y":
        # Always persist latest state before exit
        save_tasks()
        print("All tasks saved. Goodbye!")
        return True
    print("Exit cancelled.")
    return False



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
            # ▼ (4-4) Edit flow ▼
            edit_task()

        elif choice == "4":
            # ▼ (4-5) Delete flow ▼
            delete_task()

        elif choice == "5":
            # (5-5) Safe Exit: confirm + auto-save before quitting
            if confirm_exit():
                break
        else:
            print("Invalid option. Please try again.")



# ▬ (1-3) “MAIN()” FUNCTION → INTO “MAIN” BLOCK ▬
if __name__ == "__main__":
    main()

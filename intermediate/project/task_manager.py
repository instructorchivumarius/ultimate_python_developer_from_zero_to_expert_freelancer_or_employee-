# (1) Creating the CLI Interface
#     A simple command-line menu for our Task Manager project
# ___________________________________________________________


# ▬ (1-1) “SHOW MENU()” FUNCTION ▬
def show_menu():
    """Display the main menu options"""
    print("\n--- Task Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Exit")


# ▬ (1-2) “MAIN()” FUNCTION → WITH LOOP ▬
def main():
    """Main program loop that runs until user exits"""
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Viewing tasks... (to be implemented)")
        elif choice == "2":
            print("Adding a task... (to be implemented)")
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
1
tasks = []

def show_menu():
    print("\nQuickTask Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    title = input("Enter task name: ")
    priority = input("Priority (1=High, 2=Medium, 3=Low): ")
    tasks.append({"title": title, "priority": int(priority), "done": False})
    print(f"Task '{title}' added.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: (x["done"], x["priority"]))
    for idx, task in enumerate(sorted_tasks):
        status = "✓" if task["done"] else " "
        prio = {1: "High", 2: "Medium", 3: "Low"}.get(task["priority"], "Unknown")
        print(f"{idx+1}. [{status}] {task['title']} (Priority: {prio})")

def mark_done():
    view_tasks()
    idx = int(input("Enter task number to mark as done: ")) - 1
    if 0 <= idx < len(tasks):
        tasks[idx]["done"] = True
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    idx = int(input("Enter task number to delete: ")) - 1
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print(f"Deleted task: {removed['title']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

def todo_app():
    tasks = []
    while True:
        action = input("Add task or 'q' to quit:  ")
        if action == 'q':
            break
        tasks.append(action)

    print("\nYour tasks")
    for task in tasks:
        print(f" - {task}")

#run it
todo_app()
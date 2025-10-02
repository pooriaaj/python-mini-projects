shopping_list = []

def add_items(item):
    if item:
        shopping_list.append(item)
        print(f'Added: {item}')

def remove_items(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'Removed: {item}')
    else:
        print(f'Task Not Found')

def show_items():
    if shopping_list:
        for i, j in enumerate(shopping_list, start=1):
            print(f'{i}. {j}')
    else:
        print('No Items Yet')

while True:
    cmd = input("> ").strip()
    if cmd.lower() == 'quit':     # case-insensitive quit
        print('Goodbye!')
        break
    elif cmd.startswith('add '):
        add_items(cmd[4:].strip())
    elif cmd.startswith('remove '):
        remove_items(cmd[7:].strip())
    elif cmd == 'show':
        show_items()
    else:
        print("Unknown command")

filepath = 'todo.txt'

def get_todos(file_path=filepath):
    """read a text file and return a list of items """
    with open(file_path, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=filepath):
    """write items of the list to the text file"""
    with open(filepath, 'w') as file_l:
        file_l.writelines(todos_arg)


if __name__ == "__main__":
    print('Hello')

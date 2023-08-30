#!/usr/bin/python3
if __name__ == "__main__":
    """Prints all the names defined by the compiled module """
    import hidden_4
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)


def ask_overwrite_file():
    if input("File already exists, Overwrite? (y/N)") in ['y','Y']:
        return True
    else:
        return False

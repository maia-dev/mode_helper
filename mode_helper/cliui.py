
def override_file():
    if input("File already exists, Override? (y/N)") in ['y','Y']:
        return True
    else:
        return False

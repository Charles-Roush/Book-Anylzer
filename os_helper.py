import os

def check_file(path, make):
    if os.path.exists(path):
        return True
    elif make:
        try:
            os.makedirs(path)
            return True
        except Exception as e:
            print(f"Error creating directory: {e}")
            return False
    return False
        
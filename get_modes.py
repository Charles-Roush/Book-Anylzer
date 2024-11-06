import os_helper

def get_text_files():
    while True:
        text_files = input("name/names of file:\n").split()
        if 'exit' in text_files:
            break 
        if all(os_helper.check_file(book, False) == True for book in text_files):
                return text_files    
       
def get_mode():
    while True:
        is_multiple_per_file = input("multiple (m), or singular (s) per file\n").lower()
        if is_multiple_per_file == 'm':
            return True
        if is_multiple_per_file == 's':
            return False
import os_helper
    # Functions
        # check_file(dir, make) if make is true then it will make the file checked,
import plot_helper
    # Plot
# import stats_helper
import read_helper
    # read_txt(file, mode)
import get_modes

def main():
    # text_files = get_modes.get_text_files()
    # is_multiple_per_file = get_modes.get_mode()
    text_files = ['federalist_papers.txt']
    is_multiple_per_file = True
    if is_multiple_per_file == True:
        texts, numbers, names, author_list, author_works = read_helper.read_text_files(text_files, 'f')
    print(author_list)
main()
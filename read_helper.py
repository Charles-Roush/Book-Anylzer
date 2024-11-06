def read_file_federalist(file, texts, numbers, names):
    author_works = {}
    with open(file, 'r') as f:
        lines = f.read().splitlines()
        current_text = ''
        for i, line in enumerate(lines):
            if line.startswith('FEDERALIST'):
                if current_text:
                    author_works[current_name].append(current_number)
                    texts.append(current_text)
                    numbers.append(current_number)
                    names.append(current_name)

                current_number = line.split()[-1]
                current_name = ' '.join(lines[i+2].split())
                if current_name not in author_works:
                    author_works[current_name] = []
                current_text = ''
            else:
                current_text += line + ' '
        if current_text:
            author_works[current_name].append(current_number)
            texts.append(current_text)
            numbers.append(current_number)
            names.append(current_name)

    return author_works

def read_files_federalist(text_files):
    texts, numbers, names = [], [], []
    author_works = {}
    for file in text_files:
        works = read_file_federalist(file, texts, numbers, names)
        for author, works_list in works.items():
            if author not in author_works:
                author_works[author] = []
            author_works[author].extend(works_list)
    print(author_works)
    author_list = set(author_works)
    return texts, numbers, names, author_list, author_works

def read_text_files(text_files, mode):
    if mode.lower() == 'f':
        return read_files_federalist(text_files)
def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                print(line.strip())
    except Exception:
        print('Файл не найден')
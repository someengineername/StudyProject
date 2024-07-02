from contextlib import contextmanager


@contextmanager
def safe_write(file):
    temp_storage = []
    alert_flag = False

    # try to open a file if it's exists and fill up temporary storage
    try:
        with open(file, 'r', encoding='UTF-8') as open_file:
            try:
                temp_storage = open_file.readlines()
            except:
                print('no readable line')
    except:
        pass

    # open file with passed name with write-privileges (or create one)

    context_file = open(file, 'w', encoding='UTF-8')

    # try to do what's folded in context
    try:
        yield context_file
    # in case of error - print-out ExceptionName
    except Exception as e:
        alert_flag = True
        print(f'Во время записи в файл было возбуждено исключение {e.__class__.__name__}')

    # if alert flag of raised error == True, revert back all changes
    if alert_flag:
        context_file.seek(0)
        context_file.truncate(0)
        for line in temp_storage:
            context_file.write(line)

    # force-closing of opened (or created) file to finish context
    context_file.close()
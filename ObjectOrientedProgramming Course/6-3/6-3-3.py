def log_for(logfile, date_str):
    new_file_name = str('log_for_' + date_str + '.txt')
    with open(logfile, 'r', encoding='UTF-8') as input_file, open(new_file_name, 'w', encoding='UTF-8') as out_file:
        for line in input_file.readlines():
            if line[0:len(date_str)] == date_str:
                out_file.write(line[len(date_str) + 1:])
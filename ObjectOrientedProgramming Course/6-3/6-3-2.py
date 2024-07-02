def non_closed_files(files_list):
    answer = []

    for file in files_list:
        if not file.closed:
            answer.append(file)

    return answer

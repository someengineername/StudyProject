class ReadableTextFile:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        test_list1 = []
        with open(self.filename, 'r', encoding='UTF-8') as file:
            for line in file.readlines():
                test_list1.append(line.strip())
        return test_list1

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
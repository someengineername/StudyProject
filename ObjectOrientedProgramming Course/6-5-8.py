class WriteSpy:

    def __init__(self, file1, file2, to_close=False):
        self.file1 = file1
        self.file2 = file2
        self.to_close = to_close
        self.non_writable_non_open_flag = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.to_close:
            self.file1.close()
            self.file2.close()
        if self.non_writable_non_open_flag:
            raise ValueError('Файл закрыт или недоступен для записи')

    def write(self, input_str):
        if not self.file1.closed and not self.file2.closed and self.writable():
            self.file1.write(input_str)
            self.file2.write(input_str)
        else:
            self.non_writable_non_open_flag = True

    def close(self):
        self.file1.close()
        self.file2.close()

    def closed(self):
        return self.file1.closed and self.file2.closed

    def writable(self):
        if self.file1.closed or self.file2.closed:
            return False
        return self.file1.mode == 'w' and self.file2.mode == 'w'

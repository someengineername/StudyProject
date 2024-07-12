class Pagination:

    def __init__(self, input_list, page_size):

        self.db = [input_list[i:i + page_size] for i in range(0, len(input_list), page_size)]
        self.page_size = page_size
        self.total_pages = len(self.db)
        self.current_page = 1  # 0

    def prev_page(self):
        self.current_page -= 1

        if self.current_page < 1:  # 0
            self.current_page = 1  # 0
        if self.current_page > len(self.db):
            self.current_page = len(self.db)
        return self

    def next_page(self):
        self.current_page += 1

        if self.current_page < 1:  # 0
            self.current_page = 1  # 0
        if self.current_page > len(self.db):
            self.current_page = len(self.db)
        return self

    def first_page(self):
        self.current_page = 1  # 0

    def last_page(self):
        self.current_page = len(self.db)

    def go_to_page(self, index):
        self.current_page = index

        if self.current_page < 1:  # 0
            self.current_page = 1  # 0
        if self.current_page > len(self.db):
            self.current_page = len(self.db)

    def get_visible_items(self):
        return self.db[self.current_page - 1]

    def __repr__(self):
        return str(self.db)

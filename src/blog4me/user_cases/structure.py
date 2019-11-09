from abc import abstractmethod


class Provider:
    @abstractmethod
    def get_menu(self):
        pass

    @abstractmethod
    def add_page(self, page, file_name):
        pass

    @abstractmethod
    def delete_page(self, page):
        pass

    @abstractmethod
    def update_page(self, page, new_file_name):
        pass

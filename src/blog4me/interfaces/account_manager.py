from abc import abstractmethod


class Base:
    @abstractmethod
    def signin(self, username, password):
        pass

    @abstractmethod
    def create_account(self, username):
        pass

    @abstractmethod
    def delete_account(self, username):
        pass

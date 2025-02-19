class Note:
    def __init__(self, id, title, content):
        self.__id = id
        self.title = title
        self.content = content

    def __str__(self):
        return f"ID: {self.__id}, Title: {self.title}, Content: {self.content}"

    def get_id(self):
        return self.__id
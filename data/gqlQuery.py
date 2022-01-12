import string


class GqlQuery:
    def __init__(self, name: string, query: string, param: dict):
        self.param = param
        self.name = name
        self.query = query


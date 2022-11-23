class getDrink:
    def __init__(self, data: dict):
        self.data = data

    def name(self, index_number) -> int:
        return list(self.data.keys())[index_number]

    def value(self, index_number) -> int:
        return list(self.data.values())[index_number][0]

    def inventory(self, index_number) -> int:
        return list(self.data.values())[index_number][1]

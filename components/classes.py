import dataManager


# get data by self-oriented index from data with staticmethod.
class getDrink:
    # static functions returns parameters by index number, without looping.
    @staticmethod
    def name(index_number) -> int:
        return list(dataManager.drinks.types.keys())[index_number]

    @staticmethod
    def value(index_number) -> int:
        return list(dataManager.drinks.types.values())[index_number][0]

    @staticmethod
    def inventory(index_number) -> int:
        return list(dataManager.drinks.types.values())[index_number][1]

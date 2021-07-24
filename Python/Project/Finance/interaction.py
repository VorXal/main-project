class Interaction:

    @staticmethod
    def insert(spending, name, type, cost):
        spendingDocument = {
            "name": name,
            "type": type,
            "cost": cost
        }
        spending.insert_one(spendingDocument)

    @staticmethod
    def get_all(spending):
        return list(spending.find())

class User:

    def __init__(self, user, password):
        self.__user = user
        self.__password = password
        self.__connect = "mongodb+srv://"+user+":"+password+"" \
          "@financecontrol.slgh6.mongodb.net/FinanceControl?retryWrites=true&w=majority"

    def get_connect(self):
        return self.__connect

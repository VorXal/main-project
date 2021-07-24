class User:

    def __init__(self, user, password):
        self.__user = user
        self.__password = password
        self.__connect = "your"+user+":"+password+"path"

    def get_connect(self):
        return self.__connect

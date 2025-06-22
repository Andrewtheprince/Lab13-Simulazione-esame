from database.DAO import DAO


class Model:
    def __init__(self):
        pass

    @staticmethod
    def getAnni():
        return DAO.getAllAnni()
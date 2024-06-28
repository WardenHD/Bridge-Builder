'''
File that adds management for database with profiles
'''
import sqlite3

class Saves:
    '''
    This class is used to interact with the SQLite database to store and retrieve game saves.
    '''

    def __init__(self):
        '''
        Initializes the Saves class by connecting to the SQLite database.
        '''
        self.__con = sqlite3.connect('saves.sqlite', check_same_thread = False)
        self.__cursor = self.__con.cursor()

        try: self.__cursor.execute('''CREATE TABLE Saves (Id INTEGER PRIMARY KEY, Wins INT NOT NULL)''')
        except sqlite3.OperationalError: pass

        self.__con.commit()

    def add(self) -> None:
        '''
        Adds a new save to the database.
        '''
        self.__cursor.execute("INSERT INTO Saves VALUES (NULL, 0)")
        self.__con.commit()

    def get(self, id: int) -> tuple:
        '''
        Retrieves a save from the database by its ID.
        :param id: id
        :return: tuple (id, wins)
        '''
        if id < 0: raise IndexError("Index cannot be less that 1")

        self.__cursor.execute("SELECT * FROM Saves WHERE Id = ?", ([id]))
        row = self.__cursor.fetchone()
        if row is None: return None

        return (row[0], row[1])
    
    # @dispatch(int, int)
    # def get(self, wins: int) -> tuple:
    #     '''
    #     Retrieves a save from the database by its wins.
    #     :param wins: number of wins
    #     :return: tuple (id, wins)
    #     '''
    #     self.__cursor.execute("SELECT * FROM Saves WHERE Wins = ?", (wins))
    #     row = self.__cursor.fetchone()
    #     if row is None: return None

    #     return (row[0], row[1])
    
    def get_all(self) -> list[tuple]:
        '''
        Retrieves all saves from the database.
        :return: list of tuple (id, wins)
        '''
        self.__cursor.execute("SELECT * FROM Saves")
        return [(row[0], row[1]) for row in self.__cursor.fetchall()]

    
    def set(self, id: int, wins: int) -> None:
        '''
        Updates a save in the database.
        :param id: id
        :param wins: number of wins
        :param level: current level
        '''
        if id < 0: raise IndexError("Index cannot be less that 1")

        self.__cursor.execute('''UPDATE Saves SET Wins = ? WHERE Id = ?''', 
            (wins, id))
        self.__con.commit()

    def delete(self, id: int) -> None: 
        '''
        Deletes a save from the database by id.
        :param id: id to delete the save
        '''
        if id < 0: raise IndexError("Index cannot be less that 1")

        self.__cursor.execute("DELETE FROM Saves WHERE Id = ?", ([id]))
        self.__con.commit()

    def close(self):
        '''
        Commits the changes and closes the connection to the database.
        '''
        self.__con.commit()
        self.__con.close()

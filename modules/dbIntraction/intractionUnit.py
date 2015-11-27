
import sqlite3
from datetime import date

class DataBase:
    """Handles data base interactions, updates, backups"""

    __active_db__   = None
    __db_object__   = None
    __db_instance__ = None

    def __init__( db_name ):
        """ constructor for the class DataBase"""

        self.__active_db__   = db_name
        self.__db_object__   = sqlite.connect( self.__active_db__ )
        self.__db_instance__ = __db_object__.cursor()


    def create_table( table_name, table_attr ):
        """Create a new table in the database"""

        create_command = "CREATE TABLE "+table_name+" (%s)"
        self.__db_instance__.execute( create_command % table_attr )


    def drop_table( table_name ):
        """delete a  table from database"""

        drop_command = "DROP TABLE "+table_name
        self.__db_instance__.execute( drop_command )


    def insert_row( table_name, attr_values ):
        """Insert a new row in table"""

        insert_command = "INSERT INTO "+table_name+" VALUES(%s)"
        self.__db_instance__.execute( insert_command % attr_values )


   def insert_rows( table_name, attr_list, attr_values ):
        """Insert a new row in table"""

        insert_command = "INSERT INTO "+table_name+" [("+attr_list+")]"
        for value_set in attr_values:
            insert_command = insert_command+"\nVALUES (%s)" %valueset
        self.__db_instance__.execute( insert_command )


    def delete( table_name, table_attr ):
        """Create a new table in the database"""

        create_command = "CREATE TABLE "+table_name+" (%s)"
        self.__db_instance__.execute( create_command % table_attr )



# this is the page where we create our instance of a dog and all the class methods.

from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninjas_model
from flask_app import DATABASE

class Dojo:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for one_row in results:
            this_dojo_instance = cls(one_row)
            all_dojos.append(this_dojo_instance)
        return all_dojos


    @classmethod
    def get_all_dojo_participants(cls,data):
        query = """
            SELECT * FROM dojos 
            LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
            WHERE dojos.id = %(id)s
        """
        results = connectToMySQL("dojos_ninjas").query_db(query,data)
        ninja_list = []
        if results:
            dojo_instance = cls(results[0])
            for row in results:
                ninja_data = {
                    "id" : row['ninjas.id'],
                    "first_name" : row['first_name'],
                    "last_name" : row['last_name'],
                    "age" : row['age'],
                    "created_at" : row['ninjas.created_at'],
                    "updated_at" : row['ninjas.updated_at'],
                    "dojo_id" : row['dojo_id'],
                }
                ninja_instance = ninjas_model.Ninja(ninja_data)
                ninja_list.append(ninja_instance)
            dojo_instance.participants = ninja_list
            return dojo_instance
        return False

    @classmethod
    def create_dojo(cls,data):
        query = """
            INSERT INTO dojos (name)
            VALUES (%(name)s);
        """
        return connectToMySQL("dojos_ninjas").query_db(query,data)


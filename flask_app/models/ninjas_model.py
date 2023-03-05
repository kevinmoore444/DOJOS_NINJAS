from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojos_model
from flask_app import DATABASE

class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO ninjas (first_name, last_name, age, dojo_id)
            VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        return connectToMySQL("dojos_ninjas").query_db(query,data)

    
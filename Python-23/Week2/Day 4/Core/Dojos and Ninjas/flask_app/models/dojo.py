
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninja
class Dojo :
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.name = data_dict['name']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        self.my_ninjas=[]
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results,"-"*25)
        dojos = []
        for row in results:
            dojo = cls(row)
            dojo.my_ninjas = ninja.Ninja.get_dojo_ninja({'dojo_id':dojo.id})
            dojos.append(dojo)
        return dojos
    # Create
    @classmethod
    def create_dojo(cls, data):
        query = """
        INSERT INTO dojos (name)
        VALUES (%(name)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    

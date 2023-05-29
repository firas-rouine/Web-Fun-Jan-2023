from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
class Ninja :
    def __init__(self, data_dict) :
        self.id = data_dict['id']
        self.dojo_id = data_dict['dojo_id']
        self.first_name = data_dict['first_name']
        self.last_name = data_dict['last_name']
        self.age = data_dict['age']
        self.created_at = data_dict['created_at']
        self.updated_at = data_dict['updated_at']
        # self.owner = user.User.get_one({'id':self.user_id}).username
        # self.user = ""
    # CRUD Queries
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query)
        # print(results,"+*+"*25)
        ninjas = []
        for row in results:
            ninja = cls(row)
            # book.user=row["username"]
            ninjas.append(ninja)
        return ninjas
    # Create
    @classmethod
    def create_ninja(cls, data):
        query = """
        INSERT INTO ninjas (dojo_id,first_name,last_name, age)
        VALUES (%(dojo_id)s,%(first_name)s,%(last_name)s,%(age)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_dojo_ninja(cls,data):
        query = """
        SELECT * FROM ninjas WHERE dojo_id  = %(dojo_id)s;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        ninjas = []
        print(results)
        if(results):
            for row in results:
                ninjas.append(cls(row))
            return ninjas
        else:
            return [] 
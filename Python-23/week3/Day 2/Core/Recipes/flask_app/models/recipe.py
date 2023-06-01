from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
from flask_app.models import user


class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.user_id = data['user_id'] #! Must Have
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.poster = user.User.get_by_id({'id':self.user_id}).first_name
        
    # - CREAT
    @classmethod
    def create_recipe(cls, data):
        query = """
            INSERT INTO recipes (user_id,name, description, instruction, date, under)
            VALUES (%(user_id)s,%(name)s,%(description)s,%(instruction)s,%(date)s,%(under)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    
    # - GET ALL
    @classmethod
    def get_all_recipes(cls):
        query = """
            SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;; 
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for row in results:
            recipe = cls(row)
            recipe.poster = f"{row['first_name']} {row['last_name']}"
            recipes.append(recipe)
        return recipes
    
    
    @classmethod
    def get_by_id(cls,data):
        query = """
                select * from recipes
                where id =%(id)s;
                """
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results)< 1 :
            return []
        return cls(results[0])
    

    
    @classmethod
    def update_recipe(cls, data):
        query = """
            UPDATE recipes SET name =%(name)s,description =%(description)s,instruction =%(instruction)s,under =%(under)s
            WHERE id = %(id)s ;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    @classmethod
    def delete_recipes(cls, data):
        query = """
           delete from recipes where id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("name must be at  least 2 characters !")
            is_valid = False
        
        if len(data['description']) < 1:
            flash("description must be not blanc" )
            is_valid = False
        if len(data['instruction'])<1:
            is_valid = False
            flash("instruction must be not blanc")
        if data['date'] == "":
            is_valid = False
            flash("Date is required")
            
        
        return is_valid
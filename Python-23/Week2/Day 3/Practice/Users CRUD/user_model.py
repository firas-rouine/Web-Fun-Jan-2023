from mysqlconnection import connectToMySQL

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def get_all(cls):
        query = """
        select * from users;
        """
        results  = connectToMySQL("users").query_db(query)
        # print("*"*25,results,"*"*25)
        all_users=[]
        for row in results:
            user=cls(row)
            all_users.append(user)
            # print(all_users,"*"*25)
        return all_users
    @classmethod
    def create(cls,data):
        query = """
        insert into users (first_name,last_name,email)
        values (%(first_name)s,%(last_name)s,%(email)s);
        """
        result  = connectToMySQL("users").query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        result = connectToMySQL("users").query_db(query,data)
        print(result[0],"*-*"*20)
        return cls(result[0])
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s,
        email= %(email)s
        WHERE id = %(id)s;
        """
        return connectToMySQL("users").query_db(query,data)
    @classmethod
    def delete(cls, user_id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL("users").query_db(query, data)
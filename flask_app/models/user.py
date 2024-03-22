from flask_app.config.mysqlconnection import connectToMySQL
#might need other imports like flash other classes and regex

db = 'users'

class users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data ['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        pass


    @classmethod
    def userdata(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        user = []
        for data in results:
            user.append(cls(data))
        print(results)
        print(user)
        return user
    

    @classmethod
    def save(cls , data):
        query = 'INSERT INTO users (first_name , last_name , email ) VALUES ( %(first_name)s , %(last_name)s , %(email)s)'
        return connectToMySQL(db) .query_db(query , data)
    
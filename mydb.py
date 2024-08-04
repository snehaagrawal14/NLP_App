import json

class Database:
    
    def add_data(self, name, email, password):
        with open("db.json", "r") as rf:
            database = json.load(rf)
        
        if email in database:
            return 0
        database[email] = [name, password]
        with open("db.json", "w") as wf:
            json.dump(database, wf)
        return 1
    
    def search(self, email, password):
        with open("db.json", "r") as rf:
            database = json.load(rf)
            
        if email not in database:
            return -1
        return database[email][1]==password
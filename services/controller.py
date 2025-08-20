from soldier import Soldier
from querise import Querise
from connection import Connection

client = Connection()
queries = Querise(client)

class Controller():

    @staticmethod
    def get_soldiers():
        try:
            soldiers = queries.get_soldiers()
            for s in soldiers:
                s["_id"] = str(s["_id"])
            return soldiers
        except Exception as e:
            return {"Error": "Error geting all soldiers.", "message": e}, 500
        

    @staticmethod
    def update_soldier(id, data):
        try:
            result = queries.update_soldier(id, data)
            return result
        except Exception as e:
            return {"Error": "Error updateing soldier.", "message": e}


    @staticmethod
    def delete_soldier(id):
        try:
            result = queries.delete_soldier(id)
            return result
        except Exception as e:
            return {"Error": "Error deleteing soldier.", "message": e}
        
    
    @staticmethod
    def add_soldier(soldier):
        try:
            soldier_obj = Soldier(soldier["id"], soldier["first_name"], soldier["last_name"], soldier["phone_number"], soldier["rank"])
            return queries.add_soldier(soldier_obj.__dict__)
        except Exception as e:
            return {"Error": "Error adding soldier.", "message": e}
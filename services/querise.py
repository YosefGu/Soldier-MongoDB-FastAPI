

class Querise():

    def __init__(self, client):
        self.conn = client
    
    def get_soldiers(self):
        return list(self.conn.collection.find({}))
    
    def add_soldier(self, soldier):
        result = self.conn.collection.insert_one(soldier)
        return {"inserted_id": str(result.inserted_id)}
    
    def delete_soldier(self, id):
        responce = self.conn.collection.delete_one({"id" : id})
        return {"responce" : str(responce)}
    
    def update_soldier(self, id, data):
        updated_soldier = self.conn.collection.find_one_and_update(
            {"id": id}, 
            {"$set" : data},
            return_document = True
            )
        updated_soldier.pop("_id", None)
        return {"responce" : updated_soldier}
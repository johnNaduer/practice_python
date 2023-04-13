import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.data = kwargs
        
    def to_dict(self):
        obj_dict = self.__dict__.copy()
        """
        obj_dict.update(self.data)
        """
        return obj_dict

my_dict = {'name': 'Juan', 'age': 30, 'city': 'Bogotá'}
my_obj = BaseModel(**my_dict)
print(my_obj.to_dict()) # Output: {'id': '<un ID único generado por uuid.uuid4()>', 'data': {'name': 'Juan', 'age': 30, 'city': 'Bogotá'}, 'name': 'Juan', 'age': 30, 'city': 'Bogotá'}


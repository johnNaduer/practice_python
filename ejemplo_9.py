import uuid

class MyClass:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.data = {'id': self.id, **kwargs}

my_dict = {'name': 'Juan', 'age': 30, 'city': 'Bogotá'}
my_obj = MyClass(**my_dict)
print(my_obj.data)

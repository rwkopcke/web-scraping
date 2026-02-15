import requests
import json


def json_response(url):
    '''
    Docstring for json_response
    
    :param url: Description
    '''
    # yields a serialized string obj
    response = requests.get(url)
    # converts to python list of dicts
    todos = json.loads(response.text)
    #print(todos[:2])
    
    todos_by_user = dict()
    for todo in todos:
        if todo['completed']:
            try:
                todos_by_user[todo['userId']] += 1
            except:
                todos_by_user[todo['userId']] = 1

    top_users = sorted(todos_by_user.items(),
                       key= lambda x: x[1], 
                       reverse= True)
    
    max_complete = top_users[0][1]
    
    users = []
    for user, num_complete in top_users:
        if num_complete < max_complete:
            break
        users.append(str(user))
        
    max_users = " & ".join(users)
    
    print(f'user(s) {max_users} completed {max_complete} TODOS')
    
    # show items that users 5 and 10 have completed
    def keep(todo):
        is_complete = todo['completed']
        has_max_count = str(todo['userId']) in users
        return is_complete and has_max_count
    
    with open('io_main/filtered_data_file.json', 'w') as data_file:
        filtered_todos = list(filter(keep, todos))
        json.dump(filtered_todos, data_file, indent= 4)
        
        
class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
def json_custom_obj():
    '''
    Docstring for json_custom_obj
    '''
    
    # Person is not serializable, only most builtin types
    # json_str = json.dumps(Person('Will', 29))
    
    # simplifying data structures
    # what is the minimum amount of information nec to recreate obj?
    # complex data type: real value, imaginary value
    # need only to encode two floats
    
    # error
    #json_str = json.dumps(4+6j)
    # print(json_str)
    
    def complex_encoder(z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            type_name = z.__class__.__name__
            raise TypeError(f"Object of type {type_name} is not \
                JSON serializable")
        
    json_str = json.dumps(4+6j, default=complex_encoder)
    print(json_str)
    
    
class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            super().default(self, z)
    

def json_custom_encoder():
    '''
    Docstring for json_custom_encoder
    '''
    json_str = json.dumps(4+6j, cls= ComplexEncoder)
    print(json_str)
    
    
def json_decode_custom_types():
    '''
        deserialize custome types
        use meta data to know how to proceed
        e.g. the complex number
        {
            "__complex__": True,
            "real": 42,
            "imaginary": 36
        }
    '''
    
    data = \
        {
            "__complex__": True,
            "real": 42,
            "imaginary": 36
        }
    
    with open('io_main/complex_data.json', "w") as complex_data:
        json.dump(data, complex_data, indent= 4)
        
    
    def decode_complex(dct):
        if "__complex__" in dct:
            return complex(dct["real"], dct['imaginary'])
        else:
            return dct
        
    with open('io_main/complex_data.json') as complex_data:
        data = complex_data.read()
        z = json.loads(data, object_hook= decode_complex)
        
    print(z, type(z))
    print()
    
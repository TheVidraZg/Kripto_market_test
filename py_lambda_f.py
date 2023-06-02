# def suma(x, y):
#     return x + y

# s= suma(5, 10)

# print(s)

s =  lambda x, y: x+y
print(s(5,10))

class User:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
    def __str__(self) -> str:
        pass


    def set_first_name(self, first_name):
        pass
        
users = []
user =users.append(User('Pero', 'Peric'),
      users.append(User('Lav', 'Laic')),
      users.append(User('Mirko', 'Iviic')))


print(users[1])







print(users[1][0])        
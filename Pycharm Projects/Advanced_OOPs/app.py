from admin import Admin
from database import Database

a = Admin("Divya","1206",3)
a.save()

print(Database.find(lambda x:x['username'] == "Divya"))


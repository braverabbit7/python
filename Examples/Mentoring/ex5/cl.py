pk = 8756
db = {pk:["w","r","x"]}
print(db)
def users(pk,p):
    user=db[pk]
    return p in user
print(users(8756,"r"))
print(users(8756,"w"))
print(users(8756,"x"))
print(users(8756,"d"))

#Написать используя замыкание

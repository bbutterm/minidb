class user():
    name = "string"
    age = 0
    sex = 0
    # 0 = female 1 = male
    def __init__(self,name,age=0,sex=0):
        self.name = name
        self.age = age
        self.sex = sex
class mydb():
    data = {}
    size = 0
    def view(self):
        print("id ___ name___ age ___ sex")
        ids = self.data.keys()
        for i in ids:
            print(i,"___",(self.data.get(i).name),"___",(self.data.get(i).age),"___",(self.data.get(i).sex))
    def add(self,name,age = 0,sex = 0):
        self.size += 1
        new = user(name,age,sex)
        self.data[self.size] = new
    def info(self,id):
        print("Name: ",self.data.get(id).name)
        print("Age: ",self.data.get(id).age)
        if self.data.get(id).sex == 1:
            print("Sex: Male")
        else:
            print("Sex: FeMale")

    def get(self,id,info = "name"):
        if info == "name":
            return(self.data.get(id).name)
        if info == "age":
            return (self.data.get(id).age)
        if info == "sex":
            return (self.data.get(id).sex)
    def set(self,id,value,arg = 0):
        if value == "name":
            self.data.get(id).name = arg
        if value == "age":
            self.data.get(id).age = arg
        if value == "sex":
            self.data.get(id).sex = arg
            
#testing..           
db = mydb()
db.add("anya")
db.add("vasya")
db.set(1,"age",arg = 18)
db.set(1,"sex",arg = 0)
db.view()

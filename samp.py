


class Student:
    first_name="waga"
    last_name="baga"
    age = 18

    def __init__(self,first_name,last_name,age):
        self.first_name =first_name 
        self.last_name =last_name 

        if age < 18:
            self.age =18
        else:
            self.age =age 



s1 = Student("waga","baga",12) #init call 
# s2 = Student()
# s3 = Student()
# s4 = Student()
print( s1.first_name , s1.age)
    

class Customer :
    def __init__(self,code,name,phone,email):
        self.code = code
        self.name=name
        self.phone=phone
        self.email=email

    def __str__(self):
        return f"{self.code}\t{self.name}\t{self.phone}\t{self.email}"

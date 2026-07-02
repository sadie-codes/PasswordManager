class Password:
    #Class definition of each password
    #attributes include password and website name
    def __init__(self, website_name, password):
        self.website_name = website_name
        self.password = password
        
    #getter method for password
    @property
    def password_accessor():
        return self.password
        
    
    #updates password to a new password using a type of setter
    @password_accessor.setter
    def password_accessor(self, new_password):
        self.password = new_password
        
    #toString method that prints out name and website
    def toString(self):
        return "Website Name: " + self.website_name + "\nPassword: " + self.password

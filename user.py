class User:
 
 
 user_list = []

 def save_user(self):
     """
     save user method saves user objects into user_list
     """

     User.user_list.append(self)


 
 def __init__(self,firstname,lastname,username,password):

    #INSTANCE VARIABLES
    self.firstname = firstname
    self.lastname = lastname
    self.username = username
    self.password = password





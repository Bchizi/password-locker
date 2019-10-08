import string , random

class User:
 
 
    user_list = []

    def save_user(self):
        """
        save user method saves user objects into user_list
        """

        User.user_list.append(self)
    @classmethod    
    def login_authentication(cls,username,password):
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user  



    

    
 
    def __init__(self,firstname,lastname,username,password):

        #INSTANCE VARIABLES
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password


class Credentials:

    credentials_list = []
    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        ''' 
        delets the user
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name_credential(cls,username):

        for credential in cls.credentials_list:
            if credential.username == username:
                return credential
     
    @classmethod
    def display_credentials(cls):
        """
        a method that returns the credentials list
        """
        return cls.credentials_list
    @classmethod    
    def generate_password(cls,stringLength=8):
        password = string.ascii_lowercase
        return ''.join(random.choice(password) for i in range(stringLength)) 


        

    def __init__(self,social_account,social_username,social_password,username):
        self.social_account = social_account
        self.social_username = social_username
        self.social_password = social_password
        self.username = username 
    
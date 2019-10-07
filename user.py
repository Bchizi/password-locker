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


class Credentials:

    credentials_list = []
    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_user(self):
        ''' 
        delets the user
        '''
        Credentials.credentials_list.remove(self)

    def __init__(self,social_account,social_username,social_password):
        self.social_account = social_account
        self.social_username = social_username
        self.social_password = social_password

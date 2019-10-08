#!/usr/bin/env python3.7
from user import User

def create_user(fname,lname,username,password):
    '''
    Function to create a new contact
    '''
    new_user = User (fname,lname,username,password)
    return new_user

def save_user(User):
    '''
    Function to save contact
    '''
    User.save_user() 

def save_credentials(Credentials):
    """
    function to save credential
    """    
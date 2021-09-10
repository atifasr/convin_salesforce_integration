import requests
from requests.models import requote_uri
from .api_keys import access_token
from .models import *

#helper functions
def users_data():
    url = "https://d5g00000cr5k7eal-dev-ed.my.salesforce.com/services/data/v52.0/query/?q=select FIELDS(ALL) from user limit 5"
    params = {
        'Authorization':f'Bearer {access_token}'
    }
    resp = requests.get(url,headers = params)
    resp = resp.json()
    return resp

def get_accounts():
    url = "https://d5g00000cr5k7eal-dev-ed.my.salesforce.com/services/data/v52.0/query/?q=select FIELDS(ALL) from account limit 5"
    params = {
        'Authorization':f'Bearer {access_token}'
    }
    resp = requests.get(url,headers = params)
    resp = resp.json()
    return resp

def get_contacts():
    url = "https://d5g00000cr5k7eal-dev-ed.my.salesforce.com/services/data/v52.0/query/?q=select FIELDS(ALL) from contact limit 5"
    params = {
        'Authorization':f'Bearer {access_token}'
    }
    resp = requests.get(url,headers = params)
    resp = resp.json()
    return resp



#helpers for filtering data 

def account_data(resp_accounts):
    account_data_list = []
    account_data = {}
    for data in resp_accounts['records']:
        account_data['id'] = data['Id']
        account_data['Name'] = data['Name']
        account_data['PhotoUrl'] = data['PhotoUrl']
        account_data['BillingAddress'] = data['BillingAddress']
        account_data['AccountNumber'] = data['AccountNumber']
        account_data_list.append(account_data)
        account_data = {}

    return account_data_list



 #filtering contact data 

def contact_data(resp_contacts):
    contact_data_list = []
    contact_data = {}
    for data in resp_contacts['records']:
        contact_data['id'] = data['Id']
        contact_data['AccountId'] = data['AccountId']
        contact_data['LastName'] = data['LastName']
        contact_data['FirstName'] = data['FirstName']
        contact_data['Name'] = data['Name']
        contact_data['MailingStreet'] = data['MailingStreet']
        contact_data['Phone'] = data['Phone']
        contact_data['Birthdate'] = data['Birthdate']
        contact_data['LeadSource'] = data['LeadSource']
        contact_data['Email'] = data['Email']
        contact_data['Department'] = data['Department']
        contact_data['PhotoUrl'] = data['PhotoUrl']

        contact_data_list.append(contact_data)
        contact_data = {}

    return contact_data_list


def users_data_list(resp_users):
    users_data_list = []
    user_data = {}
    for data in resp_users['records']:
        user_data['id'] = data['Id']
        user_data['Username'] = data['Username']
        user_data['LastName'] = data['LastName']
        user_data['FirstName'] = data['FirstName']
        user_data['CompanyName'] = data['CompanyName']
        user_data['City'] = data['City']
        user_data['TimeZoneSidKey'] = data['TimeZoneSidKey']
        user_data['AboutMe'] = data['AboutMe']
        user_data['Phone'] = data['Phone']
        user_data['Email'] = data['Email']
        user_data['IsActive'] = data['IsActive']
        users_data_list.append(user_data)
        user_data = {}

    return users_data_list






#bulk insert 

def insert_data(fetched_data):
    accounts_dt, contact_dt, users_dt = fetched_data
    data_list = []
    for data in accounts_dt:
        data_list.append(AccountData(account_id = data['id'],
        name=data['Name'],
        photourl=data['PhotoUrl'],
        billingaddress = data['BillingAddress'],
        account_number = data['AccountNumber']))
    AccountData.objects.bulk_create(data_list)

    data_list = []
    for data in contact_dt:
        data_list.append(ContactData(contact_id= data['id'],
        accountid=data['AccountId'],
        lastname = data['LastName'],
        firstname=data['FirstName'],
        name=data['Name'],
        mailingstreet = data['MailingStreet'],
        phone_no = data['Phone'],
        birth_day = data['Birthdate'],
        lead_source = data['LeadSource'],
        email = data['Email'],
        department = data['Department'],
        photourl =data['PhotoUrl']
        ))
    ContactData.objects.bulk_create(data_list)
        

    data_list = []
    for data in users_dt:
        data_list.append(UserData(
            user_id = data['id'],
            username= data['Username'],
            lastname=data['LastName'],
            firstname= data['FirstName'],
            company_name = data['CompanyName'],
            city =data['City'],
            timezonesidekey =data['TimeZoneSidKey'],
            aboutme = data['AboutMe'],
            email = data['Email'],
            isactive = data['IsActive']

        ))
    UserData.objects.bulk_create(data_list)


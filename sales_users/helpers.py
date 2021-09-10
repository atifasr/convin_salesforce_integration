import requests
from requests.models import requote_uri
from .api_keys import access_token


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
        contact_data['MobilePhone'] = data['MobilePhone']
        contact_data['Birthdate'] = data['Birthdate']
        contact_data['LeadSource'] = data['LeadSource']
        contact_data['Email'] = data['Email']
        contact_data['Department'] = data['Department']
        contact_data['PhotoUrl'] = data['PhotoUrl']

        contact_data_list.append(contact_data)
        contact_data = {}

    return contact_data_list
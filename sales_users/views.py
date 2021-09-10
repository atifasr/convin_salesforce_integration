from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import requests
import concurrent
from .helpers import *
from django.core.exceptions import *
from django.db import IntegrityError
from .models import AccountData,UserData,ContactData
# Create your views here.


def index(request):
    if request.method == 'GET':

        return render(request,'sales_users/index.html')


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




#fetch data from external Salesforce API's 
def get_data(request):
    if request.method == 'GET':
        resp_accounts = resp_users = resp_contacts  = None
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future = executor.submit(get_accounts)
            future2 = executor.submit(users_data)
            future3 = executor.submit(get_contacts)
            resp_accounts = future.result()
            resp_users = future2.result()
            resp_contacts = future3.result()

            
        # using helper functionsin helpers.py
        accounts_data = account_data(resp_accounts)
        contact_data_list = contact_data(resp_contacts)
        user_data_list = users_data_list(resp_users)

        
        data = [accounts_data,contact_data_list,user_data_list]

        # pushing data when query parameter push is true
        push = request.GET.get('push')
        if push:
            insert_data(data)
            return redirect('/view_data/')
      

        data = {
           'data':data
        }
               
        return render(request,'sales_users/index.html',data)



#store data in database and display it after retrieving
def view_data(request):
    if request.method == 'GET':
        accounts_data = AccountData.objects.all()
        users_det = UserData.objects.all()
        contact_det = ContactData.objects.all()
        error = None
        try:

            pass
        except ObjectDoesNotExist:
            print('data already exists')
            error = 'data already exists'

        return render(request,'sales_users/list.html',{
            'error':error,
            'accounts_data':accounts_data
        })






from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from .api_keys import access_token
from concurrent.futures import ThreadPoolExecutor
from .helpers import *
# Create your views here.


def index(request):
    if request.method == 'GET':

        return render(request,'sales_users/index.html')


#fetching data from these function


#fetch data from external Salesforce API's 
def get_data(request):
    if request.method == 'GET':
        resp_accounts = resp_users = resp_contacts  = None
        with ThreadPoolExecutor(max_workers=4) as executor:
            future = executor.submit(get_accounts)
            future2 = executor.submit(users_data)
            future3 = executor.submit(get_contacts)
            resp_accounts = future.result()
            resp_users = future2.result()
            resp_contacts = future3.result()

            

        accounts_data = account_data(resp_accounts)
        contact_data_list = contact_data(resp_contacts)

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
            users_data_list.append(user_data)
            user_data = {}

        print(users_data_list)


        # print(account_data_list)

        return render(request,'sales_users/index.html',{
            'data':None
        })



def view_data(request):
    if request.method == 'GET':
        return render(request,'sales_users/list.html')
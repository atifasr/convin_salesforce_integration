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
        error = None

        try:
            accounts_data = AccountData.objects.all()
            users_det = UserData.objects.all()
            contact_det = ContactData.objects.all()
            data = {
                'accounts_data':accounts_data,
                'users_det':users_det,
                'contact_det':contact_det,
            }
        except ObjectDoesNotExist:
            print('data already exists')
            error = 'data already exists'
            data = None

        return render(request,'sales_users/list.html',{
            'error':error,
            'data_context':data
        })






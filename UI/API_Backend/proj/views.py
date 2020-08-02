from django.shortcuts import render
import csv
# import pyrebase
from pymongo import MongoClient
import datetime
from django.http import JsonResponse

# config = {
#     'apiKey': "AIzaSyBSyiGygAJST4sfy2vKnakRkwlRDNWzKus",
#     'authDomain': "siht20.firebaseapp.com",
#     'databaseURL': "https://siht20.firebaseio.com",
#     'projectId': "siht20",
#     'storageBucket': "siht20.appspot.com",
#     'messagingSenderId': "1051406150301",
#     'appId': "1:1051406150301:web:77571113ba1452007dc274",
#     'measurementId': "G-VN0Y1F08EK"
#   }

# firebase = pyrebase.initialize_app(config)
# auth = firebase.auth()
# db = firebase.database()


def upload(request):
    return render(request, 'upload.html')

def post_upload(request):
    csv_file = request.FILES.get('csv_file')
    decoded_file = csv_file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)

    client = MongoClient('mongodb+srv://abhip1912:abcd1234@cluster0.ywymp.mongodb.net/<dbname>?retryWrites=true&w=majority')
    db = client.get_database('Demo')
    records = db.Blacklist

    # for row in reader:
    #     data ={ 'url': row.get('url'), 'lable': row.get('lable') }
    #     print(str(data))
    #     db.child('urls').child(counter).set(data)
    #     counter += 1

    # for row in reader:
    #     data = {'url':row.get('url')}
    #     db.child('blacklist').child(counter).set(data)
    #     counter += 1

    all_new = []
    counter = 0
    for row in reader:
        data = {'url':row.get('url')}
        all_new.append(data)
        counter += 1
    records.insert_many(all_new)
    return render(request, 'upload.html')

def home(request):
    if request.method == "POST":
        url_link = request.POST.get('url')
        
    e = {'domain_name': 'AMBERLYROBINSON.COM', 'registrar': 'GoDaddy.com, LLC', 'whois_server': 'whois.godaddy.com', 'referral_url': None, 'updated_date': [datetime.datetime(2018, 10, 18, 16, 58, 39), datetime.datetime(2018, 10, 18, 16, 58, 38)], 'creation_date':
        datetime.datetime(2008, 10, 17, 17, 47, 17), 'expiration_date': datetime.datetime(2020, 10, 17, 17, 47, 17), 'name_servers': ['NS1.BLUDOMAIN50.COM', 'NS2.BLUDOMAIN50.COM'], 'status': ['clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited',
        'clientRenewProhibited https://icann.org/epp#clientRenewProhibited', 'clientTransferProhibited https://icann.org/epp#clientTransferProhibited', 'clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited', 'clientTransferProhibited http://www.icann.org/epp#clientTransferProhibited',
        'clientUpdateProhibited http://www.icann.org/epp#clientUpdateProhibited', 'clientRenewProhibited http://www.icann.org/epp#clientRenewProhibited', 'clientDeleteProhibited http://www.icann.org/epp#clientDeleteProhibited'], 'emails': ['abuse@godaddy.com',
        'AMBERLYROBINSON.COM@domainsbyproxy.com'], 'dnssec': 'unsigned', 'name': 'Registration Private', 'org': 'Domains By Proxy, LLC', 'address': ['DomainsByProxy.com', '14455 N. Hayden Road'], 'city': 'Scottsdale', 'state': 'Arizona', 'zipcode': '85260',
        'country': 'US'}
    return render(request, 'layout.html', {'e':e.items()})


def feedback(request):
    client = MongoClient('mongodb+srv://abhip1912:abcd1234@cluster0.ywymp.mongodb.net/<dbname>?retryWrites=true&w=majority')
    db = client.get_database('Demo')
    records = db.feedback

    name = request.POST['name']
    email = request.POST['email']
    msg = request.POST['msg']
    data = {'name':name, 'email':email, 'msg':msg}
    records.insert_one(data)
    return render(request, 'layout.html')
from django.shortcuts import render
import csv
# import pyrebase
from pymongo import MongoClient


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

    client = MongoClient('mongodb+srv://abhip1912:<password>@cluster0.ywymp.mongodb.net/<dbname>?retryWrites=true&w=majority')
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

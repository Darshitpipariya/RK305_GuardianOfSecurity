from django.shortcuts import render
import pyrebase
from pymongo import MongoClient
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers
from django.conf import settings
import json


client = MongoClient('mongodb+srv://abhip1912:<password>@cluster0.ywymp.mongodb.net/<dbname>?retryWrites=true&w=majority')
db = client.get_database('Demo')
records = db.Blacklist


@api_view(["POST"])
def task(data):
  data = json.loads(data.body)
  link = data['url']

  db_resp = list(records.find({'url':link}))
  if len(db_resp) >= 1:
    data = {link:'1'}
    return JsonResponse(data, safe=False)

  data = {link:'0'}
  return JsonResponse(data, safe=False)

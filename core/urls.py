from django.urls.resolvers import URLPattern
from core.views import get_Automated_Id, set_Record , get_Record
from re import search
from django.urls import path
# from .views import 

URLPattern[
    path("search/",get_Record,name ="get_Record"),
    path("create/",set_Record,name = "set_Record"),
    path("id/",get_Automated_Id, name = "get_Automated_id")
]
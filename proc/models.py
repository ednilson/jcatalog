# coding: utf-8

from mongoengine import *
import datetime


connect('journals-catalog')


class Scielo(DynamicDocument):
    creation_date = DateTimeField(default=datetime.datetime.now)
    is_scielo = IntField(required=True)
    issn_list = ListField()


class Scimago(DynamicDocument):
    creation_date = DateTimeField(default=datetime.datetime.now)
    is_scimago = IntField(required=True)
    issn_list = ListField()


class Scopus(DynamicDocument):
    creation_date = DateTimeField(default=datetime.datetime.now)
    is_scopus = IntField(required=True)


class Scopus_Discontinued(DynamicDocument):
    pass


class Jcr(DynamicDocument):
    creation_date = DateTimeField(default=datetime.datetime.now)
    is_jcr = IntField(required=True)


class Cwts(DynamicDocument):
    creation_date = DateTimeField(default=datetime.datetime.now)
    is_cwts = IntField(required=True)
    issn_list = ListField()

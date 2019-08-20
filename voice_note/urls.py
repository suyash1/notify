'''
All urls reside here.
To add any new endpoint, import corresponding class from views.py
and add a url handler in __init__ method
'''
from flask_restful import Api
from voice_note import app_trigger
from voice_note.views import AppHealth, TopicProducer

api = Api(app_trigger)

class APIClass(object):
    '''
    Class containing all URL endpoints
    '''
    def __init__(self):
        api.add_resource(AppHealth, '/health')
        api.add_resource(TopicProducer, '/publish_note')

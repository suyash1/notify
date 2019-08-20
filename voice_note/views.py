"""
@author: Suyash
This file contains all the view functions linked to urls
"""
import json

from flask_restful import Resource, Api, reqparse
from flask import request
from voice_note import app_trigger
from voice_note.producer.push_to_topic import Producer

api = Api(app_trigger)
parser = reqparse.RequestParser()


# all url handlers goes here

class AppHealth(Resource):
    """
    AppHealth health method
    """

    def get(self):
        """
        HTTP GET method
        """
        return {"Alive": True}


class TopicProducer(Resource):
    """
    A simple producer API that will be triggered once the voice
    recording is done. For the demo, this is synchronous call
    but depending upon the async requirement, this can be modified
    to non-blocking call
    Enhancements: exception handling
    """

    def post(self):
        args = request.get_json()
        print(args)
        file_path = args.get('file_path')
        pilot_id = args.get('pilot_id')
        producer = Producer()
        producer.connect(exchange=args.get('exchange'))
        print(file_path, pilot_id, args.get('exchange'), args.get('topic'))
        msg = producer.publish(topic=args.get('topic'), message=json.dumps({'pilot_id': pilot_id,
                                                                            'audio_file': file_path}))
        producer.close()
        return json.dumps(msg), 200


# url handlers end here

from voice_note.urls import APIClass

APIClass()

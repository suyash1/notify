'''
first file to be executed in Application
'''
from flask import Flask
import os
envt = os.environ.get("APP_ENV")

app_trigger = Flask(__name__)
if envt == 'PROD':
    app_trigger.config.from_object('config.ProductionConfig')
elif envt == 'STAG':
    app_trigger.config.from_object('config.StagingConfig')
else:
    app_trigger.config.from_object('config.DeveloperConfig')

import voice_note.views

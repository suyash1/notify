'''
@author: Suyash Srivastava
file to run application in blocking mode
'''
from voice_note import app_trigger

if __name__ == '__main__':
    app_trigger.run(host='127.0.0.1', port=8010, debug=True)

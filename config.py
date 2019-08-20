'''
All the project configuration goes here
@Author: Suyash
'''

class BaseConfig(object):
    '''
    base configuraion common to all
    '''
    APP_NAME = 'Pre-Launch'
    APP_VERSION = '0.0.1'
    

class DeveloperConfig(BaseConfig):
    '''
    Developer config goes here specific to dev envt
    '''
    pass

class StagingConfig(BaseConfig):
    '''
    Staging config will be used on staging server
    '''
    pass

class ProductionConfig(BaseConfig):
    '''
    Production config goes here
    '''
    pass

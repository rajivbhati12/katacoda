import os
import requests 
#from hamcrest import *

@given('I have {test_api} url')
def step_impl(context,test_api):
    context.test_api_url=os.environ.get(test_api.upper() + '_URL')


@when('I call a get request')
def step_impl(context):
    print(">>>>>>" + context.test_api_url)
    context.response = requests.get(url = context.test_api_url)


@then('I should get \'Hello World\' in response')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get \'Hello World\' in response')


@then('the response status is 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response status is 200')

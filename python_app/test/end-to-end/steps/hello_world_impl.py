import os
import requests 
import env as ENV


@given('I have Hello World url')
def step_impl(context):
    context.test_api_url=ENV.HELLO_WORLD_URL


@when('I call a get request')
def step_impl(context):
    context.response = requests.get(url = context.test_api_url)
	

@then('I should get \'{message}\' in response')
def step_impl(context, message):
    assert message in context.response.text 


@then('the response status is 200')
def step_impl(context):
    assert int(context.response.status_code) == 200    

import os
from hamcrest import *

@given(u'I have Hello_World url')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have Hello_World url')


@when(u'I call a get request')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I call a get request')


@then(u'I should get \'Hello World\' in response')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should get \'Hello World\' in response')


@then(u'the response status is 200')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the response status is 200')

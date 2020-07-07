Feature: Hello World Api
Scenario: User get 'Hello World' in response
	Given I have Hello World url
	When I call a get request
	Then I should get 'Hello World' in response
	And the response status is 200

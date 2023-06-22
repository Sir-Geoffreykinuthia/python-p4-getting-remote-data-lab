import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)
    
# THis prints the data in our terminal as json data
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
people_data = get_requester.load_json()
print(people_data)

# But the printed data is not being indented 
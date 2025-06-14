import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        name = "howard"

        name_formatted = name.replace(" ", "+")
        fields = ["name", "occupation"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

        response = requests.get(URL)
        return response.content

    def load_json(self):
        name = "howard"

        name_formatted = name.replace(" ", "+")
        fields = ["name", "occupation"]
        fields_formatted = ",".join(fields)
        limit = 1

        URL = f"https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        print(URL)
        response = requests.get(URL)
        return response.json()
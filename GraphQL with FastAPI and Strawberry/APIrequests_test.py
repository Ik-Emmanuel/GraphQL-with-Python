import requests
import json

# import pandas as pd

query1 = """
        {
        blogs  {
        id
        title

        }
    }
"""
query2 = """
        mutation{
        addPost(title:"The API test  Title", content:"This ApI test one", author:"Mac Anthony")
        {
            title
            author
        }
}
"""

url = 'http://localhost:8000/graphql'
r = requests.post(url, json={'query': query1})
print(r.status_code)
json_data = json.loads(r.text)
print(json_data['data'])
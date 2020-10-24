import database
import requests
import json

test_db = database.Database("e12cf059-45c3-4649-937a-3a6c345029dd", "us-east1", "StartupCentral", "JacobIsTheBest", "SocialMedaDB")

# https://e12cf059-45c3-4649-937a-3a6c345029dd-us-east1.apps.astra.datastax.com/api/rest/v1/auth

url = "https://e12cf059-45c3-4649-937a-3a6c345029dd-us-east1.apps.astra.datastax.com/api/rest/v1/keyspaces/{keyspace}/tables".format(keyspace=test_db.keyspace)

payload = {
    "name": "testTable",
    "ifNotExists": True,
    "columnDefinitions": [{"name":"testField1", "typeDefinition":"text", "static":True}],
    "primaryKey": 
    {
        "partitionKey": ["testField1"]
    }
}

headers = {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "X-Cassandra-Token": test_db.token,
    "X-Cassandra-Request-Id": "de3112d5-e41f-3a13-80ba-783b8d311107"
}

response = requests.request("POST", url, data=json.dumps(payload), headers=headers)

print(response.text)
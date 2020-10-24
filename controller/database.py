import requests
import json
import uuid


url = "https://databaseid-region.apps.astra.datastax.com/api/rest/v1/"

key = "e12cf059-45c3-4649-937a-3a6c345029dd"
region = "us-east1"
keyspace = "SocialMedaDB"

class Database:
    
    def __init__(self, uuid, region, db_username, password, keyspace):
        self.db_uuid = uuid
        self.region = region
        self.url = "https://{db_uuid}-{region}.apps.astra.datastax.com/api/rest/v1/".format(db_uuid=self.db_uuid, region=self.region)
        self.username = db_username
        self.password = password
        self.keyspace = keyspace

        def auth():
            url = self.url + "auth"
            # url = "https://e12cf059-45c3-4649-937a-3a6c345029dd-us-east1.apps.astra.datastax.com/api/rest/v1/auth"

            headers = {
                "Accept": "*/*",
                "Content-Type": "application/json"
            }

            body = {
                "username": self.username,
                "password": self.password
            }

            response = requests.request("POST", url, data=json.dumps(body), headers=headers)

            token = json.loads(response.text)["authToken"]

            self.token = token

        auth()

    def getUser(self, email):
        url = self.url + "keyspaces/{keyspace}/tables/{userTable}/rows/{primaryKey}".format(keyspace=self.keyspace, userTable="Users", primaryKey=email)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def getProject(self, project):
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows/{primaryKey}".format(keyspace=self.keyspace, userTable="Users", primaryKey=project)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("GET", url, headers=headers)

    
    
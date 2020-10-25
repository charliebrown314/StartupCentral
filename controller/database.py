import requests
import json
import uuid

from model.backendDefs import Dev, Project

url = "https://databaseid-region.apps.astra.datastax.com/api/rest/v1/"

key = "e12cf059-45c3-4649-937a-3a6c345029dd"
region = "us-east1"
keyspace = "SocialMedaDB"


class Database:

    def __init__(self, uuid, region, db_username, password, keyspace):
        self.db_uuid = uuid
        self.region = region
        self.url = "https://{db_uuid}-{region}.apps.astra.datastax.com/api/rest/v1/".format(db_uuid=self.db_uuid,
                                                                                            region=self.region)
        self.username = db_username
        self.password = password
        self.keyspace = keyspace
        self.token = None

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
        url = self.url + "keyspaces/{keyspace}/tables/{userTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                            userTable="Users",
                                                                                            primaryKey=email)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("GET", url, headers=headers)

        print(response.text)

    def setUser(self, dev_class: Dev):
        url = self.url + "keyspaces/{keyspace}/tables/{userTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                            userTable="Users",
                                                                                            primaryKey=dev_class.developer)
        payload = {"changeset": [
            {
                "value": {"email": dev_class.developer, "first_name": dev_class.firstname,
                          "join_date": dev_class.joinDate,
                          "last_name": dev_class.lastName, "last_session": dev_class.lastSession,
                          "projects": set(dev_class.projects), "tags": set(dev_class.tags)},
                "column": "data"
            }
        ]}

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("PUT", url, json=payload, headers=headers)

        print(response.text)

    def getProject(self, project):
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                               userTable="Projects",
                                                                                               primaryKey=project)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("GET", url, headers=headers)

    def setProject(self, project_class: Project):
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                               userTable="Projects",
                                                                                              primaryKey=project_class.projectName)
        payload = {"changeset": [
            {
                "value": {"active": project_class.active, "created_date": project_class.createdDate,
                          "description": project_class.description,
                          "dev_list": project_class.developers, "manager": project_class.manager,
                          "name": set(project_class.projectName), "tags": set(project_class.currentTags)},
                "column": "data"
            }
        ]}
        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("PUT", url, json=payload, headers=headers)

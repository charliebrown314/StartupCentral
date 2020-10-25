import requests
import json
import uuid
from typing import List

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

    def getUser(self, email) -> Dev:
        url = self.url + "keyspaces/{keyspace}/tables/{userTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                            userTable="Users",
                                                                                            primaryKey=email)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": str(uuid.uuid1())
        }

        response = requests.request("GET", url, headers=headers)

        dev_obj = json.loads(response.text)["rows"][0]["data"]
        return Dev(firstName=dev_obj["first_name"], joinDate=dev_obj["join_date"], lasName=dev_obj["last_name"],
                   developer=dev_obj["email"], tags=dev_obj["tags"], currentProjects=dev_obj["projects"],
                   lastSession=dev_obj["last_session"])

    def setUser(self, dev_class: Dev) -> None:
        url = self.url + "keyspaces/{keyspace}/tables/{userTable}/rows".format(keyspace=self.keyspace,
                                                                               userTable="Users")
        payload = {"columns": [
            {
                "name": "tags",
                "value": dev_class.tags
            },
            {
                "name": "projects",
                "value": dev_class.projects
            },
            {
                "name": "last_session",
                "value": dev_class.lastSession
            },
            {
                "name": "join_date",
                "value": dev_class.joinDate
            },
            {
                "name": "last_name",
                "value": dev_class.lastName
            },
            {
                "name": "first_name",
                "value": dev_class.firstname
            },
            {
                "name": "name",
                "value": dev_class.developer
            }
        ]}

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": str(uuid.uuid1())
        }

        requests.request("POST", url, json=payload, headers=headers)

    def getProject(self, name) -> Project:
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows/{primaryKey}".format(keyspace=self.keyspace,
                                                                                               projectTable="Projects",
                                                                                               primaryKey=name)

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": uuid.uuid1()
        }

        response = requests.request("GET", url, headers=headers)
        project_obj = json.loads(response.text)["rows"][0]["data"]
        return Project(project_obj["active"], project_obj["created_date"], project_obj["description"],
                       project_obj["dev_list"], project_obj["manager"], project_obj["name"], project_obj["tags"])

    def setProject(self, project_class: Project) -> None:
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows".format(keyspace=self.keyspace,
                                                                                  projectTable="Projects")
        payload = {"columns": [
            {
                "name": "tags",
                "value": project_class.projectName
            },
            {
                "name": "manager",
                "value": project_class.projectName
            },
            {
                "name": "dev_list",
                "value": project_class.projectName
            },
            {
                "name": "description",
                "value": project_class.projectName
            },
            {
                "name": "created_date",
                "value": project_class.projectName
            },
            {
                "name": "active",
                "value": project_class.active
            },
            {
                "name": "name",
                "value": project_class.projectName
            }
        ]}
        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": str(uuid.uuid1())
        }

        requests.request("POST", url, json=payload, headers=headers)

    def getProjectNames(self) -> List[str]:
        url = self.url + "keyspaces/{keyspace}/tables/{projectTable}/rows".format(
            keyspace=self.keyspace,
            projectTable="Projects")

        headers = {
            "Accept": "application/json",
            "X-Cassandra-Token": self.token,
            "X-Cassandra-Request-Id": str(uuid.uuid1())
        }

        response = requests.request("GET", url, headers=headers)
        return [i["name"] for i in json.loads(response.text)["rows"]]

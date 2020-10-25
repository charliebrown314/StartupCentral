import requests
import json

from controller.database import Database
from model.backendDefs import Project
import datetime

test_db = Database("e12cf059-45c3-4649-937a-3a6c345029dd", "us-east1", "StartupCentral", "JacobIsTheBest", "SocialMedaDB")


print(test_db.getProjectNames())

p = Project(True, datetime.datetime.now(),"weak ass description", ["Joe", "Jacob", "Macias", "Nick"],"Jacob","StartupCentral",["tired","python"])

test_db.setProject(p)

print(test_db.getProjectNames())
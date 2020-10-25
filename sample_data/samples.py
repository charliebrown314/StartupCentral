from datetime import datetime
import random

from model.backendDefs import Project

desc = "this is the generic description that I don't modify"
emails = ["jwbrown4@buffalo.edu", "jacobsny@buffalo.edu", "jmacias@buffalo.edu", "nmacrae@buffalo.edu", "johntant@buffalo.edu", "smalinow@buffalo.edu","johnduna@buffalo.edu"]
tags = ["python","flask","opencv","C","CQL","SQL","Django","Java","Javascript","web-app","OOP","Inheritance","Polymorphism"]
p = Project(True, datetime.now(),"A Startup Centric Social Media Application to Encourage Creative Collisions", ["jwbrown4@buffalo.edu", "jacobsny@buffalo.edu", "jmacias@buffalo.edu", "nmacrae@buffalo.edu"],"jacobsny@buffalo.edu","StartupCentral",["python"])

p_list = []
for i in range(20):
    p_list.append(Project(random.choice([True, False]), datetime.now(), desc, random.choices(emails, k=4),random.choice(emails),"Project{}".format(i), random.choices(tags,k=6)))


def load():
    return [p] + p_list

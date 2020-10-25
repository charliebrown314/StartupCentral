from datetime import datetime
import random

from model.backendDefs import Project, Dev

desc = "this is the generic description that I don't modify"
emails = ["jwbrown4@buffalo.edu", "jacobsny@buffalo.edu", "jmacias@buffalo.edu", "nmacrae@buffalo.edu", "johntant@buffalo.edu", "smalinow@buffalo.edu","johnduna@buffalo.edu"]
tags = ["python","flask","opencv","C","CQL","SQL","Django","Java","Javascript","web-app","OOP","Inheritance","Polymorphism"]
p = Project(True, datetime.now(),"A Startup Centric Social Media Application to Encourage Creative Collisions", ["jwbrown4@buffalo.edu", "jacobsny@buffalo.edu", "jmacias@buffalo.edu", "nmacrae@buffalo.edu"],"jacobsny@buffalo.edu","StartupCentral",["python"])
names = {"jwbrown4@buffalo.edu":("Joe","Brown"), "jacobsny@buffalo.edu":("Jacob","Snyderman"), "jmacias@buffalo.edu":("Jon","Macias"), "nmacrae@buffalo.edu":("Nick","Macrae"), "johntant@buffalo.edu":("John","Tantillo"), "smalinow@buffalo.edu":("Stephen","Malinowski"),"johnduna@buffalo.edu":("John","Dunaske")}

p_list = [p]
d_list = [Dev(names[e][0],datetime.now(),names[e][1],e,[],[],datetime.now()) for e in emails]
for i in range(20):
    p_list.append(Project(random.choice([True, False]), datetime.now(), desc, random.choices(emails, k=4),random.choice(emails),"Project{}".format(i), random.choices(tags,k=6)))
for p in p_list:
    for d in p.developers:
        d.updateAddProjects([p.projectName])
        l = [t for t in random.choices(p.tags, k=2) if t not in d.tags]
        d.updateTagAdd(l)




def load():
    return p_list,d_list

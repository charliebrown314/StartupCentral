from controller.database import Database
from model.Devs import Dev
from model.modeling import Model


class Projects:
    def __init__(self, APIkey:str, region:str, username:str, password:str, keyspace:str):
        self.DB : Database = Database(APIkey, region, username, password, keyspace)
        self.pnames = self.DB.getProjectNames()
        self.projects = [self.DB.getProject(i) for i in self.pnames]
        self.Model = Model([[p.projectName] + p.currentTags for p in self.projects])
        self.devs = []
        for p in self.projects:
            for d in p.developers:
                if d not in self.devs:
                    self.devs.append(d)
        self.devs = [self.DB.getUser(d) for d in self.devs]

    def dev_recommendation(self,tags):
        return self.Model.dev_recommendation(tags,[[d.developer,d.firstname,d.lastName]+d.tags for d in self.devs])

    def proj_recommendation(self, p_name):
        return self.Model.recommendations(p_name)

    def addDev(self,fname,time,lname,email):
        new_dev = Dev(fname, time, lname, email, [], [],time)

        self.projects.DB.setUser(new_dev)

    def refresh_struct(self):
        self.pnames = self.DB.getProjectNames()
        self.projects = [self.DB.getProject(i) for i in self.pnames]
        self.Model = Model([p.project] + p.tags for p in self.projects)
        self.devs = [self.DB.getUser(d) for d in sum([p.developers for p in self.projects])]
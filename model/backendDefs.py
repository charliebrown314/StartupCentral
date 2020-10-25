import time

#keys for the dictionary in JS should be projectName, devList, tags, date, active, description, manager
#may need functionality for the removal of devs


#active(boolean), created_date (date), description (text), dev_list(list<text>)., manager (text),
# name (text), tags(set<text>)
from controller.database import Database
from model.modeling import Model


class Projects:
    def __init__(self):
        self.DB = Database("e12cf059-45c3-4649-937a-3a6c345029dd", "us-east1", "StartupCentral", "JacobIsTheBest", "SocialMedaDB")
        self.pnames = self.DB.getProjectNames()
        self.projects = [self.DB.getProject(i) for i in self.pnames]
        self.Model = Model([p.project] + p.tags for p in self.projects)
        self.devs = [self.DB.getUser(d) for d in sum([p.developers for p in self.projects])]

    def dev_recommendation(self,tags):
        return self.Model.dev_recommendation(tags,[[d.developer,d.firstname,d.lastName]+d.tags for d in self.devs])

    def proj_recommendation(self, p_name):
        return self.Model.recommendations(p_name)

    def refresh_struct(self):
        self.pnames = self.DB.getProjectNames()
        self.projects = [self.DB.getProject(i) for i in self.pnames]
        self.Model = Model([p.project] + p.tags for p in self.projects)
        self.devs = [self.DB.getUser(d) for d in sum([p.developers for p in self.projects])]



class Project:

#active == active and is a boolean
#created  is the date that it was created == created_date is a date (assuming text)
#description is the project description == description
#developerlist is the list of current developers on the project == dec_list [MUST BE CONVERTED TO SET]
#manager is the manager of the current project == manager
#project is the name of the current project == name
#tags is the set of current tags == tags

    active : bool
    createdDate : time
    description : str
    developerList : list
    manager : str
    project : str
    tags : list

    def __init__(self ,active : bool, created : time, description : str, developerList : list, manager : str, projects: str, tags : list):
        self.active = active
        self.createdDate = created
        self.description = description
        self.developers = developerList
        self.manager = manager
        self.projectName = projects
        self.currentTags = tags

#this is going to take in the currrent List of addDevList, the set will not allow duplicates so no  checking needed
    def updateAddDevList(self, addDevList):
        currentDevList = self.developerss
        for developer in addDevList:
            currentDevList.add(developer)
        return currentDevList

#removes developers in the set to remove from the project set, discrad wil not throw an error if the tag does not exist
    def updateRemoveDevList(self, removeDevList):
        currentDevList = self.developers
        for developer in removeDevList:
            currentDevList.discard(developer)
        return currentDevList

    def updateAddTags(self, addTagList):
        currentTagSet = self.currentTags
        for tag in addTagList:
            currentTagSet.add(tag)
        return currentTagSet

    def updateRemoveTags(self, removeTagList):
        currentTagSet = self.currentTags
        for tag in removeTagList:
            currentTagSet.discard(tag)
        return currentTagSet

#This is going to take in a boolean value only
    def updateActive(self, value):
        currentStatus = self.active
        currentStatus = value
        return currentStatus

#for now this function will completely the current description.
    def updateDescription(self, newDescription):
        currentDescription = self.description
        currentDescription = newDescription
        return currentDescription

    def UpdateManager(self, newManager):
        currentManager = self.manager
        currentManager = newManager
        return currentManager





#email (text) first_name(text), joint_ date (date), last_name (text) last_session(timestamp)
# projects(set<text>), tags(set<text>)
class Dev:

#developer list is the list of developers, developer should be the email == email
#tags is the set of tags == tags
# current projects is the set of current projects == projects
#lastSession is the last time the develper was online this is a timestamp
#lastName == last_name
#firstName == first_name
#join_date == joinDate


    def __init__(self, firstName, joinDate, lasName, developer, tags, currentProjects, lastSession):
        self.firstname = firstName
        self.joinDate = joinDate
        self.lastName = lasName
        self.developer = developer
        self.tags = tags
        self.projects = currentProjects
        self.lastSession = lastSession

    def updateTagAdd(self, addlist):
        #taglist may have to have element from dev
        currentDeveloper = self.developer
        for tag in addlist:
            currentDeveloper.add(tag)
        return currentDeveloper

    def updateTagRemove(self, removeList):
        #taglist may have to have element from dev
        currentDeveloper = self.developer
        for tag in removeList:
            currentDeveloper.discard(tag)
        return currentDeveloper

    def updateAddProjects(self, addProjectList):
        #this will take in a list of projects and a developer and update the developer
        #need to confirm where the items are held
        developerProjects = self.projects
        for project in addProjectList:
            developerProjects.add(project)
        return developerProjects

    def updateRemoveProjects(self, removeProjectList):
        #this will take in a list of projects and a developer and update the developer
        #need to confirm where the items are held
        developerProjects = self.projects
        for project in removeProjectList:
            developerProjects.discard(project)
        return developerProjects

    def updateLastSession(self, lastSession):
        currenttime = time.time()
        lastOnline = currenttime
        return lastOnline
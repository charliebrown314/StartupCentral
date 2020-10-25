from datetime import date

#keys for the dictionary in JS should be projectName, devList, tags, date, active, description, manager
#may need functionality for the removal of devs

class Project:

#projectList is the total list of prejects (the total object), tags is the list of currentTags,
#current Developer list is the list of the current delevopers for the project, description is the descritption of the
#current project, active is if the project is currently active,

    def __init__(self, projectList,currentTags, developerList, description, active):
        self.projectList = projectList
        self.currentTags = currentTags
        self.devloperList = developerList
        self.description = description
        self.active = active

    def updateDevList(self):

        return 0

    def updateTags(self):
        return 0

    def updateActive(self):
        return 0

    def updateDescription(self):
        return 0

    def UpdateManager(self):
        return 0



class Dev:

#developer list is the list of developers, developer should be the email, tags is the set of tags, current projects is the set of current projects,
#lastSession is the last time the develper was online

    def __init__(self, developerlist, developer, tags, currentProjects, lastSession):
        self.developer = developer
        self.tags = tags
        self.projects = currentProjects
        self.lastSession = lastSession
        self.developerList = developerlist

    def getDevList(self):
        devs = self.developerList
        return None

    def updateTagAdd(self, addlist):
        #taglist may have to have element from dev
        currentDeveloper = self.developer
        for tag in addlist:
            currentDeveloper.add(tag)
        return currentDeveloper

    def updateTagRemove(self, removeList):
        #taglist may have to have element from dev
        for tag in removeList:
            currentDeveloper.discard(tag)
        return currentDeveloper

    def updateAddProjects(self, addProjectList):
        #this will take in a list of projects and a developer and update the developer
        #need to confirm where the items are held
        developerProjects = self.currentProjects
        for project in addProjectList:
            developerProjects.add(project)
        return developerProjects

    def updateRemoveProjects(self, removeProjectList):
        #this will take in a list of projects and a developer and update the developer
        #need to confirm where the items are held
        developerProjects = self.currentProjects
        for project in removeProjectList:
            developerProjects.discard(project)
        return developerProjects

    def updateLastSession(self, lastSession):
        currenttime = date.today()
        lastOnline = currenttime
        return lastOnline

    def updateLastname(self):


        return None
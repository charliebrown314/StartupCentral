import time

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
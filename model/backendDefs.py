from datetime import date

#keys for the dictionary in JS should be projectName, devList, tags, date, active, description, manager
#may need functionality for the removal of devs


#active(boolean), created_date (date), description (text), dev_list(list<text>)., manager (text),
# name (text), tags(set<text>)

class Project:

#active == active and is a boolean
#created  is the date that it was created == created_date is a date (assuming text)
#description is the project description == description
#developerlist is the list of current developers on the project == dec_list [MUST BE CONVERTED TO SET]
#manager is the manager of the current project == manager
#project is the name of the current project == name
#tags is the set of current tags == tags

    def __init__(self, projectList ,active, created, description, developerList, manager, project, tags):
        self.projectList = projectList
        self.active = active
        self.createdDate = created
        self.description = description
        self.devlopers = developerList
        self.manager = manager
        self.projectName = project

#this is going to take in the currrent List of addDevList, the set will not allow duplicates so no  checking needed
    def updateAddDevList(self, addDevList):
        currentDevList = self.developerList
        for developer in addDevList:
            currentDevList.add(developer)
        return currentDevList

#removes developers in the set to remove from the project set, discrad wil not throw an error if the tag does not exist
    def updateRemoveDevList(self, removeDevList):
        currentDevList = self.developerList
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
    def updateDescription(self):

        return

    def UpdateManager(self):
        return 0



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


    def __init__(self, developerlist, firstName, joinDate, lasName, developer, tags, currentProjects, lastSession):
        self.developerList = developerlist
        self.firstname = firstName
        self.joinDate = joinDate
        self.lastName = lasName
        self.developer = developer
        self.tags = tags
        self.projects = currentProjects
        self.lastSession = lastSession
        self.developerList = developerlist  #this is the list of all developers does this need to be removed?

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
        currentDeveloper = self.developer
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
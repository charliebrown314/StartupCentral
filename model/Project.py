from datetime import time


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
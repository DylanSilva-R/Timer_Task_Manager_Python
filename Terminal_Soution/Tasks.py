
"""
This class will handle task management.
    - Create a list.
    - Add to a list.
    - Remove task from the list.
    - print list
"""

class TasksObj:
    taskCount = 0

    def __init__(self):
        self.taskList = []

    def addToList(self,taskDetails):
        # Add details to list.
        newTaskDetail = str(self.taskCount) + ") " + taskDetails
        self.taskList.insert(self.taskCount, newTaskDetail)
        self.taskCount += 1

    def removeList(self, index):
        # Remove data from the list.
        self.taskList.remove(int(index))
        self.taskCount -= 1

    def printList(self):
        # Print data from the list.
        print("")
        length = len(self.taskList)
        for x in range(length):
            print(self.taskList[x])
        print("")
    
    def getTaskCount(self):
        return self.taskCount
    
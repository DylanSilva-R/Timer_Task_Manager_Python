
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

    def add_To_List(self,taskDetails):
        # Add details to list.
        self.taskList.insert(self.taskCount, taskDetails)
        self.taskCount += 1

    def remove_List(self, index):
        # Remove data from the list.
        del self.taskList[index]
        self.taskCount -= 1

    def print_List(self):
        # Print data from the list.
        print("")
        length = len(self.taskList)
        for x in range(length):
            print(str(x) + ")" + self.taskList[x])
        print("")

    def update_List_Data(self):
        newCount = 0

        for x in range(self.taskCount):
            print()
        return
    
    def get_Task_Count(self):
        return self.taskCount
    
from CourseCatalogNode import *
from Event import *

class CourseCatalog:
    def __init__(self):
        self.root = None

# addcourse is put and helper from textbook example
    def addCourse(self, department, courseId, courseName, lecture, sections):
        department = department.upper()
        courseName = courseName.upper()
        newNode = CourseCatalogNode(department, courseId, courseName, lecture, sections)
        if self.root:
            if self._put(self.root, newNode):
                return True
            return False
        else:
            self.root = newNode
            return True

# this is the helper method to help recursively walk down the tree
    def _put(self, currentNode, newNode):
        if (newNode.department, newNode.courseId) == (currentNode.department, currentNode.courseId):
            return False
        if (newNode.department, newNode.courseId) < (currentNode.department, currentNode.courseId):
            if currentNode.left:
                return self._put(currentNode.left, newNode)
            else:
                currentNode.left = newNode
                newNode.parent = currentNode
                return True
        else:
            if currentNode.right:
                return self._put(currentNode.right, newNode)
            else:
                currentNode.right = newNode
                newNode.parent = currentNode
                return True


    def addSection(self, department, courseId, section): # returns node(payload) for key AND THEN appends a new section to its sections list if the node exists
        department = department.upper()
        res = self._get(self.root, department, courseId)
        if res:
            res.sections.append(section)
            return True
        return False


    def _get(self, currentNode, department, courseId):
        if not currentNode:
            return None
        elif (currentNode.department, currentNode.courseId) == (department, courseId):
            return currentNode
        elif (department, courseId) < (currentNode.department, currentNode.courseId):
            return self._get(currentNode.left, department, courseId)
        else:
            return self._get(currentNode.right, department, courseId)


    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):
        ret = ""
        if currentNode != None:
            ret += self._inOrder(currentNode.left)
            ret += str(currentNode)
            ret += self._inOrder(currentNode.right)
        return ret

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):
        ret = ""
        if currentNode != None:
            ret += str(currentNode)
            ret += self._preOrder(currentNode.left)
            ret += self._preOrder(currentNode.right)
        return ret

    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):
        ret = ""
        if currentNode != None:
            ret += self._postOrder(currentNode.left)
            ret += self._postOrder(currentNode.right)
            ret += str(currentNode)
        return ret

    def getAttendableSections(self, department, courseId, availableDay, availableTime):
        department = department.upper()
        res = self._get(self.root, department, courseId)
        if res is None:
            return ""

        result = ""
        for section in res.sections:
            if (section.day == availableDay and
                    availableTime[0] <= section.time[0] and
                    section.time[1] <= availableTime[1]):
                result += str(section) + "\n"
        return result



    def countCoursesByDepartment(self):
        department_counts = {}

        def countNodes(currentNode):
            if currentNode is None:
                return

            if currentNode.department in department_counts:
                department_counts[currentNode.department] += 1
            else:
                department_counts[currentNode.department] = 1


            countNodes(currentNode.left)
            countNodes(currentNode.right)


        countNodes(self.root)
        return department_counts


    def removeCourse(self, department, courseId):
        department = department.upper()
        # The first task is to find the node to delete by searching the tree
        # If the tree has more than one node we search using the _get method to find the TreeNode that needs to be removed.
        nodeToRemove = self._get(self.root, department, courseId)
        if nodeToRemove:
            if nodeToRemove == self.root and nodeToRemove.left is None and nodeToRemove.right is None:
                print("case 1")
                self.root = None
                return True
            else:
            # If the tree only has a single node, that means we are removing the root of the tree,
            # but we still must check to make sure the key of the root matches the key that is to be deleted
                self.remove(nodeToRemove)
                return True
        return False #key is not found, False is returned


    def remove(self, currentNode):
        # if node to be deleted has no children
        if currentNode.left is None and currentNode.right is None:
            if currentNode == currentNode.parent.left:
                currentNode.parent.left = None
            else:
                currentNode.parent.right = None

        # Case 3: Node to remove has both children
        elif currentNode.right != None and currentNode.left != None:
            # Need to find the successor, remove successor, and replace
            # currentNode with successor's data / payload
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.department = succ.department
            currentNode.courseId = succ.courseId
            currentNode.courseName = succ.courseName
            currentNode.lecture = succ.lecture
            currentNode.sections = succ.sections

        # Case 2: if node has a single child

        else:
            # node has left child
            if currentNode.left:
                if currentNode.parent:
                    if currentNode == currentNode.parent.left:
                        currentNode.parent.left = currentNode.left
                    else:
                        currentNode.parent.right = currentNode.left
                else: #currentNode is the root
                    self.root = currentNode.left #currentNode is the root
                currentNode.left.parent = currentNode.parent #update parent

            # if Node has right child
            elif currentNode.right:
                #node has right child only
                if currentNode.parent:
                    if currentNode == currentNode.parent.left:
                        currentNode.parent.left = currentNode.right
                    else:
                        currentNode.parent.right = currentNode.right

                else:
                    self.root = currentNode.right  # currentNode is the root
                currentNode.right.parent = currentNode.parent  # Update parent

    def removeSection(self, department, courseId, section):
        department = department.upper()
        node = self._get(self.root, department, courseId)
        if node is None:
            return False
        if section in node.sections:
            node.sections.remove(section)
            return True
        return False




'''
# create one lecture event
lecture = Event("TR", (1530, 1645), "td-w 1701")

# create four section events
section1 = Event("W", (1400, 1450), "north hall 1109")
section2 = Event("W", (1500, 1550), "north hall 1109")
section3 = Event("W", (1600, 1650), "north hall 1109")
section4 = Event("W", (1700, 1750), "girvetz hall 1112")
sections = [section1, section2, section3, section4]

# initialize a CMPSC 9 course node
node = CourseCatalogNode("cmpsc", 9, "intermediate python", lecture, sections)

print(node)

cc = CourseCatalog()
lecture = Event("TR", (1530, 1645), "TD-W 1701")
section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
sections = [section1, section2, section3, section4]
cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
section5 = Event("F", (0, 2359), "Fluent Python in One Day Hall 101")
cc.addSection("CMPSC", 9, section5)

output = cc.inOrder()
print("Output of inOrder():\n", output)

pre_order_output = cc.preOrder()
print("Output of preOrder():\n", pre_order_output)

print("Task: find all cmpsc 9 sections held on Wednesday and within 15:00 - 17:00 time period")
print(cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700)))

print("Task: count courses by department")
print(cc.countCoursesByDepartment())
'''

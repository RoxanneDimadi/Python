from Event import *

class CourseCatalogNode:
    def __init__(self, department, courseId, courseName, lecture, sections):
        self.left = None
        self.right = None
        self.parent = None
        self.department = department.upper()
        self.courseName = courseName.upper()
        self.courseId = courseId
        self.lecture = lecture
        self.sections = sections


    def __str__(self):
        s = "{} {}: {}\n".format(self.department, self.courseId, self.courseName)
        s += " * Lecture: {}\n".format(self.lecture)
        for section in self.sections:
            s += " + Section: {}\n".format(section)
        return s


    def findSuccessor(self):
        succ = None
        # Check if node has a right subtree...
        if self.right:
            # traverse through left children (min)
            succ = self.right.findMin()
#        else:
 #           if self.parent:
 #               if self.left == self.parent.left:
 #                   succ = self.parent
 #               else:
 #                   self.parent.right = None
 #                   succ = self.parent.findSuccessor()
 #                   self.parent.right = self
        return succ



    # Find minimum value in a subtree by walking down the left children
    def findMin(self):
        current = self
        while current.left:
            current = current.left
        return current

    # Used to delete the successor
    def spliceOut(self):
        # Case 1:
        # If node to be removed is a leaf, set parent's left or right
        # child references to None
        if self.left is None and self.right is None:
            if self == self.parent.left:
                self.parent.left = None
            else:
                self.parent.right = None
        # Case 2:
        # Not a leaf node. Should only have a right child for BST
        # removal
        elif self.right:
            if self == self.parent.left:
                self.parent.left = self.right
            else:
                self.parent.right = self.right
            self.right.parent = self.parent


    # Note: This code only goes through the findSuccessor and spliceOut functionality necessary
    # for BST maintenance. There are more general cases that the textbook covers that you should
    # read through and understand
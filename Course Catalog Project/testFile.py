from Event import *
from CourseCatalogNode import *
from CourseCatalog import *

    # --- Event.py ---

def test_event():
    e1 = Event("TR", (1530, 1645), "td-w 1701")
    e2 = Event("TR", (1530, 1645), "td-w 1702")
    assert e1 != e2
    assert str(e1) == "TR 15:30 - 16:45, TD-W 1701"

'''
    # --- CourseCatalogNode.py ---
def test_CourseCatalogNode():
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

    expected_output = (
        "CMPSC 9: INTERMEDIATE PYTHON\n"
        " * Lecture: TR 15:30 - 16:45, TD-W 1701\n"
        " + Section: W 14:00 - 14:50, NORTH HALL 1109\n"
        " + Section: W 15:00 - 15:50, NORTH HALL 1109\n"
        " + Section: W 16:00 - 16:50, NORTH HALL 1109\n"
        " + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n"
    )
    assert node == expected_output
'''
    # ----- Course Catalog.py ----

def test_addCourse():
    cc = CourseCatalog()
    # add a new course: cmpsc 9
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)

    arts_lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", arts_lecture, sections)


def test_addSection():
    # add a new section to cmpsc 9
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    assert True == cc.addSection("cmpsc", 9, section5)



def test_in_orderTraversals():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
    section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("CMPSC", 9, section5)

    #now the art course node
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)
    output = cc.inOrder()

    expected_in_order = (
        "ART 10: INTRODUCTION TO PAINTING\n"
        " * Lecture: TR 13:00 - 15:50, ARTS 2628\n"
        "CMPSC 9: INTERMEDIATE PYTHON\n"
        " * Lecture: TR 15:30 - 16:45, TD-W 1701\n"
        " + Section: W 14:00 - 14:50, NORTH HALL 1109\n"
        " + Section: W 15:00 - 15:50, NORTH HALL 1109\n"
        " + Section: W 16:00 - 16:50, NORTH HALL 1109\n"
        " + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n"
        " + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n"
    )
    assert cc.inOrder() == expected_in_order

def test_preOrderTraversal():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
    section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("CMPSC", 9, section5)

    # now the art course node
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

    output = cc.preOrder()

    expected_pre_order = (
        "CMPSC 9: INTERMEDIATE PYTHON\n"
        " * Lecture: TR 15:30 - 16:45, TD-W 1701\n"
        " + Section: W 14:00 - 14:50, NORTH HALL 1109\n"
        " + Section: W 15:00 - 15:50, NORTH HALL 1109\n"
        " + Section: W 16:00 - 16:50, NORTH HALL 1109\n"
        " + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n"
        " + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n"
        "ART 10: INTRODUCTION TO PAINTING\n"
        " * Lecture: TR 13:00 - 15:50, ARTS 2628\n"
    )
    assert cc.preOrder() == expected_pre_order

def test_postOrderTraversal():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
    section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("CMPSC", 9, section5)

    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "introduction to painting", lecture, sections)

    output = cc.postOrder()

    expected_post_order = (
        "ART 10: INTRODUCTION TO PAINTING\n"
        " * Lecture: TR 13:00 - 15:50, ARTS 2628\n"
        "CMPSC 9: INTERMEDIATE PYTHON\n"
        " * Lecture: TR 15:30 - 16:45, TD-W 1701\n"
        " + Section: W 14:00 - 14:50, NORTH HALL 1109\n"
        " + Section: W 15:00 - 15:50, NORTH HALL 1109\n"
        " + Section: W 16:00 - 16:50, NORTH HALL 1109\n"
        " + Section: W 17:00 - 17:50, GIRVETZ HALL 1112\n"
        " + Section: F 00:00 - 23:59, FLUENT-PYTHON-IN-ONE-DAY HALL 101\n"
    )
    assert cc.postOrder() == expected_post_order

def test_getAttendableSections():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
    section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("CMPSC", 9, section5)

    output = cc.getAttendableSections("cmpsc", 9, "W", (1500, 1700))

    expected_output = (
        "W 15:00 - 15:50, NORTH HALL 1109\n"
        "W 16:00 - 16:50, NORTH HALL 1109\n"
    )

    assert output == expected_output

def test_countCoursesByDepartment():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    section1 = Event("W", (1400, 1450), "NORTH HALL 1109")
    section2 = Event("W", (1500, 1550), "NORTH HALL 1109")
    section3 = Event("W", (1600, 1650), "NORTH HALL 1109")
    section4 = Event("W", (1700, 1750), "GIRVETZ HALL 1112")
    sections = [section1, section2, section3, section4]
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture, sections)
    section5 = Event("F", (0, 2359), "fluent-python-in-one-day hall 101")
    cc.addSection("CMPSC", 9, section5)
    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    cc.addCourse("art", 10, "introduction to painting", lecture, sections)
    output = cc.countCoursesByDepartment()
    expected_output = (
        {'ART': 1, 'CMPSC': 1}
    )
    assert output == expected_output

def test_deleteSingleRoot():
    # this is test for delete single root
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "TD-W 1701")
    sections = []  # Assuming no sections for simplicity
    department = "CMPSC"
    courseId = "9"
    courseName = "Intermediate Python"
    cc.addCourse(department, courseId, courseName, lecture, sections)

    result = cc.removeCourse("CMPSC", "9")
    assert result is True
    assert cc.root is None

    # Attempt to remove again to check proper handling of non-existent nodes
    result1 = cc.removeCourse(department, courseId)
    assert result1 is False

    #now attempt to delete a key that doesn't exist
    assert cc.removeCourse("CMPSC", "1") is False

def test_deleteRootOneChild():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "TD-W 1701")
    lecture2 = Event("TR", (1200, 1315), "TD-W 1705")
    sections1 = []  # Assuming no sections for simplicity
    sections2 = []  # Assuming no sections for simplicity
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture1, sections2)

    lecture = Event("TR", (1300, 1550), "arts 2628")
    sections = []
    assert True == cc.addCourse("art", 10, "into to paint", lecture, sections)

    # Delete the root node, which has one child
    result = cc.removeCourse("CMPSC", 9)
    assert result is True
    assert cc.root is not None
    assert cc.root.courseId == 10
    assert cc.root.courseName == "INTO TO PAINT"

def test_deleteNodeNoChildren():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "TD-W 1701")
    lecture2 = Event("TR", (1200, 1315), "TD-W 1705")
    lecture3 = Event("TR", (1300, 1550), "arts 2628")
    lecture4 = Event("TR", (1100, 1315), "arts 1300")
    sections1 = []  # Assuming no sections for simplicity
    sections2 = []  # Assuming no sections for simplicity
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture1, sections2)
    cc.addCourse("CMPSC", 16, "C++", lecture2, sections2)
    cc.addCourse("CMPSC", 5, "Comp Sci 5", lecture3, sections2)
    cc.addCourse("CMPSC", 2, "Comp Sci 2", lecture4, sections2)

    result = cc.removeCourse("CMPSC", 16)
    assert result is True
    node = cc._get(cc.root, "CMPSC", 9)
    assert node.right is None or node.right.courseId != 16

def test_deleteNodeOneChild():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "TD-W 1701")
    lecture2 = Event("TR", (1200, 1315), "TD-W 1705")
    lecture3 = Event("TR", (1300, 1550), "arts 2628")
    lecture4 = Event("TR", (1100, 1315), "arts 1300")
    sections1 = []  # Assuming no sections for simplicity
    sections2 = []  # Assuming no sections for simplicity
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture1, sections2)
    cc.addCourse("CMPSC", 16, "C++", lecture2, sections2)
    cc.addCourse("CMPSC", 5, "Comp Sci 5", lecture3, sections2)
    cc.addCourse("CMPSC", 2, "Comp Sci 2", lecture4, sections2)

    result = cc.removeCourse("CMPSC", 5)
    assert result is True

    assert cc._get(cc.root, "CMPSC", 5) is None

    # Verify the child CMPSC 2 is now connected correctly in the tree
    parent_of_child = cc._get(cc.root, "CMPSC", 2).parent
    assert parent_of_child is not None and parent_of_child.courseId == 9

def test_deleteNodeWithTwoChildren():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "TD-W 1701")
    lecture2 = Event("TR", (1200, 1315), "TD-W 1705")
    lecture3 = Event("TR", (1300, 1550), "arts 2628")
    lecture4 = Event("TR", (1100, 1315), "arts 1300")
    lecture5 = Event("TR", (1630, 1745), "TD-W 1701")
    lecture6 = Event("TR", (1800, 1915), "TD-W 1705")
    sections1 = []  # Assuming no sections for simplicity
    sections2 = []  # Assuming no sections for simplicity
    cc.addCourse("CMPSC", 9, "Intermediate Python", lecture1, sections2)
    cc.addCourse("CMPSC", 16, "C++", lecture2, sections2)
    cc.addCourse("CMPSC", 5, "Comp Sci 5", lecture3, sections2)
    cc.addCourse("CMPSC", 2, "Comp Sci 2", lecture4, sections2)
    cc.addCourse("CMPSC", 17, "Comp Sci 17", lecture5, sections2)
    cc.addCourse("CMPSC", 18, "Comp Sci 18", lecture6, sections2)

    assert cc.root.courseId == 9
    result = cc.removeCourse("CMPSC", 9)
    assert result is True
    assert cc.root.courseId != 9
    new_root = cc._get(cc.root, "CMPSC", 16)
    if new_root and new_root.left:
        assert new_root.left.courseId == 5
        assert new_root.right.courseId == 17

def test_removeSection():
    cc = CourseCatalog()
    lecture = Event("TR", (1530, 1645), "td-w 1701")
    section1 = Event("W", (1400, 1450), "north hall 1109")
    section2 = Event("W", (1500, 1550), "north hall 1109")
    section3 = Event("W", (1600, 1650), "north hall 1109")
    section4 = Event("W", (1700, 1750), "girvetz hall 1112")
    sections = [section1, section2, section3, section4]
    assert True == cc.addCourse("cmpsc", 9, "intermediate python", lecture, sections)
    assert True == cc.removeSection("cmpsc", 9, section2)

    assert cc.removeSection("CMPSC", 9, section2) == False
    course_node = cc._get(cc.root, "CMPSC", 9)
    assert section2 not in course_node.sections


def test_deleteNodeWithTwoChildren1():
    cc = CourseCatalog()
    lecture1 = Event("TR", (1530, 1645), "TD-W 1701")
    lecture2 = Event("TR", (1200, 1315), "TD-W 1705")
    lecture3 = Event("TR", (1300, 1550), "ARTS 2628")
    lecture4 = Event("TR", (1100, 1315), "ARTS 1300")
    sections = []

    # Adding courses such that the node for CMPSC 16 will have two children
    cc.addCourse("CMPSC", 16, "Data Structures", lecture2, sections)
    cc.addCourse("CMPSC", 9, "Introduction to Programming", lecture1, sections)
    cc.addCourse("CMPSC", 24, "Advanced Programming", lecture3, sections)
    cc.addCourse("CMPSC", 32, "Machine Learning", lecture4, sections)

    # CMPSC 16 should be the root in this setup and should have two children
    # Deleting the root which has two children to test proper restructuring
    assert cc.removeCourse("CMPSC", 16) == True


    new_root = cc.root
    assert new_root.department == "CMPSC"
    assert new_root.courseId == 24  # This would depend on your successor logic; it's 24 based on smallest larger node


import requests
from bs4 import BeautifulSoup

# Prepend to relative URLs
baseUrl = "https://www.port.ac.uk"
# The page that lists courses
# TODO Pagination or pass params to grab all courses
courseListUrl = "https://www.port.ac.uk/study/courses"
# CSS selector to ge the hyperlinked headers
courseLinksQuery = ".Content .o-Grid h2>a"
# Store course info here
courseList = []

# Get and parse course listings
courseListPageSource = requests.get(courseListUrl)
parsedCourseList = BeautifulSoup(courseListPageSource.text, 'html.parser')

# Get the name and URL for each course
courses = parsedCourseList.select(courseLinksQuery)
print("There are " + str(len(courses)) + " courses")
for course in courses:
    currentCourseInfo = {}
    currentCourseInfo["name"] = course.text
    currentCourseInfo["url"] = course['href']
    courseList.append(currentCourseInfo)

# Get each course
for course in courseList:
    fullURL = baseUrl + course["url"]
    coursePage = requests.get(fullURL)
    coursePageSource = BeautifulSoup(coursePage.text, 'html.parser')
    fileName = "downloads/" + course["name"] + ".html"
    print(fileName)
    with open(fileName, "w") as f:
        f.write(coursePageSource.prettify())

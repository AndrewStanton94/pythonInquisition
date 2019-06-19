import requests
from bs4 import BeautifulSoup

baseUrl = "https://www.port.ac.uk"
courseListUrl = "https://www.port.ac.uk/study/courses"
courseLinksQuery = ".Content .o-Grid h2>a"
courseList = []

page = requests.get(courseListUrl)

soup = BeautifulSoup(page.text, 'html.parser')

courses = soup.select(courseLinksQuery)

print("There are " + str(len(courses)) + " courses")

for course in courses:
    currentCourseInfo = {}
    name = course.text
    print(name)
    currentCourseInfo["name"] = name
    currentCourseInfo["url"] = course['href']
    courseList.append(currentCourseInfo)

for course in courseList[0:1]:
    fullURL = baseUrl + course["url"]
    print(fullURL)
    coursePage = requests.get(fullURL)
    coursePageSource = BeautifulSoup(coursePage.text, 'html.parser')
    prettySource = coursePageSource.prettify()
    # print(prettySource)
    fileName = course["name"] + ".html"
    print(fileName)
    with open(fileName, "w") as f:
        f.write(prettySource)

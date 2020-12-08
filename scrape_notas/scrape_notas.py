from bs4 import BeautifulSoup
import requests
import materias


SAIA_URLS = {
    "LOGIN_URL": "https://saia.psm.edu.ve/login/index.php",
    "REQUEST_URL": "https://saia.psm.edu.ve/grade/report/user/index.php?id="
}

USER_INFO = {
    "username": "Tu nombre de usuario SAIA va aqui",
    "password": "Tu contraseña va aqui"
}


def get_assignment_names(course_name, course_id, soup):
    """
    [Gets the names of the assignments that are available in 
    the course and returns a dictionary with the data obtained]

    Args:
        course_name ([string]): [string that contains the name of the course]
        course_id ([string]): [string containing the id to access the corresponding course page]
    """
    DATA_TO_SCRAPE = {
        "TAG": "a",
        "CLASS_": "gradeitemheader"
    }

    course_template = {
        "course_name": course_name,
        "course_id": course_id,
        "assigment_names": []
    }

    # Getting Data
    assignments_name_scraped = soup.find_all(DATA_TO_SCRAPE["TAG"],
                                             class_=DATA_TO_SCRAPE["CLASS_"])

    # Storing Data
    for name in assignments_name_scraped:
        course_template["assigment_names"].append(name.get_text())

    return course_template

def get_assignment_grades(soup):
    """
    [Gets information about grades and return the grades and grade range]
    """
    DATA_TO_SCRAPE = {
        "TAG": "td",
        "CLASS_": [
            "level2 leveleven item b1b itemcenter column-grade",
            "level2 leveleven item b1b itemcenter column-range"
        ]
    }

    course = {
        "grades": [],
        "grades_range": []
    }

    # Getting Data
    grades_scraped = soup.find_all(DATA_TO_SCRAPE["TAG"],
                                   DATA_TO_SCRAPE["CLASS_"][0])

    grades_range_scraped = soup.find_all(DATA_TO_SCRAPE["TAG"],
                                         DATA_TO_SCRAPE["CLASS_"][1])

    # Storing Data
    for values in zip(grades_scraped, grades_range_scraped):
        grade = values[0].get_text()
        grade_range = values[1].get_text()

        course["grades"].append(grade)
        course["grades_range"].append(grade_range)

    return course

def scrape_course_data(course_info, user_info, urls):
    """[scrape the course name, assignment name and student grades]

    Args:
        course_info ([Dictionary])
        user_info ([Dictionary])
        urls ([Dictionary])

    Returns:
        [Dictionary]: [returns the union of all the collected information]
    """
    course_name = course_info["course_name"]
    course_id = course_info["course_id"]

    with requests.Session() as session:
        post = session.post(urls["LOGIN_URL"], data=user_info)
        req = session.get(str(urls["REQUEST_URL"] + course_id))

        page = req.text
        soup = BeautifulSoup(page, "html.parser")

        assignments = get_assignment_names(course_name, course_id, soup)
        grades = get_assignment_grades(soup)
    
    return {**assignments, **grades}

def format_course_data(course_data):
    print(f"Materia: {course_data['course_name']}", end="\n\n")
    
    for index, assignment_name in enumerate(course_data["assigment_names"]):
        print(f"* Actividad {index + 1}: {assignment_name}", end="\n\n")

        print(f"\tNota \t Rango de la Nota")
        print(f"\t {course_data['grades'][index]} \t {course_data['grades_range'][index]}", end="\n\n")

if __name__ == "__main__":
    example = scrape_course_data(materias.ING_ECONOMICA, USER_INFO, SAIA_URLS)
    format_course_data(example)  

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
# print(results.prettify())

# returns an iterable for all the job listings on that page
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="subtitle")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

# finding jobs that match python
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

# allows jobElements in python_jobs to access all inforamtion by fetching from great grandpartnds element instead
python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

print(len(python_jobs))

# printing out title, location, and company of python jobs
for jobElements in python_job_elements:
    titleElement = jobElements.find("h2", class_="title")
    companyElement = jobElements.find("h3", class_="company")
    locationElement = jobElements.find("p", class_="location")
    print(titleElement.text.strip())
    print(companyElement.text.strip())
    print(locationElement.text.strip())
    print()

# Getting all the job links
for job_element in python_job_elements:
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(link.text.strip())

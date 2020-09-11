import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Seattle'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

# after inspecting the elements of the web, we know the tags, and class od each element to use in the next piece of code
# print(results.prettify())

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')

    if None in (title_elem, company_elem, location_elem):
        continue

    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

# python_jobs = results.find_all('h2', string='Python Developer')
python_jobs = results.find_all('h2', string=lambda text: 'python' in text.lower())
print(len(python_jobs))

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")
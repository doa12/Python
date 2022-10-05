"""
from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # write your ✨magical✨ code here
  else:
    print("Can't get jobs.")

extract_jobs("rust")
"""

from bs4 import BeautifulSoup
import requests


def get_jobs(keyword):
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  # user-agent???
  request = requests.get(url, headers={"User-Agent": "bubble"})
  results = []
  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    # tr???
    jobs = soup.find_all("tr", class_="job")
    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      if company:
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if location:
        location = location.string.strip()

      if company and position and location:
        job = {
          'company': company,
          'position': position,
          'location': location
        }
        results.append(job)
  else:
    print("NO MATCHING RESULTS.")
  return results

# golang???
jobs = get_jobs("golang")
print(jobs)

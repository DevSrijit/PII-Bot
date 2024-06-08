import requests
import json
import spacy
from dotenv import load_dotenv
import os

# Load the English language model
nlp = spacy.load("en_core_web_sm")

load_dotenv()  # This line brings all environment variables from .env into os.environ

# Access GitHub token securely (e.g., from environment variable)
github_token = os.environ['GITHUB_TOKEN']
github_url = "https://api.github.com"
repo_name = "personal-website-2.0"
username = "devsrijit"


# Set up PII detection
pii_entities = ["PERSON", "NORP", "ORG", "GPE", "LOC", "DATE", "TIME", "EVENT"]


def scan_data(url, data_type):
  headers = {'Authorization': f"Bearer {github_token}"}
  response = requests.get(url, headers=headers)

  if response.status_code == 200:
    data = json.loads(response.text)
    for item in data:
      if isinstance(item, dict):
        description = item.get('body', "")  # Use get() with default ""
        if description:  # Check if description is not empty
          doc = nlp(description)
          for ent in doc.ents:
            if ent.label_ in pii_entities:
              # Construct the full URL using base URL, repo name, and issue/pull number
              if data_type == "pull request":
                data_type = "pull"
              else:
                data_type = "issues"
              full_url = f"https://github.com/{username}/{repo_name}/{data_type}/{item['number']}"
              print(f"PII detected in {data_type} {item['number']}: {full_url}")
  else:
    print(f"Error fetching {data_type} data: {response.status_code}")


# Scan issues and pull requests (consider pagination for large repos)
issues_url = f"{github_url}/repos/{username}/{repo_name}/issues"
pulls_url = f"{github_url}/repos/{username}/{repo_name}/pulls"

scan_data(issues_url, "issue")
scan_data(pulls_url, "pull request")

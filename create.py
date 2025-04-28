import requests
import os

CLOUDFLARE_API_TOKEN = os.environ['CF_API_TOKEN']  # or set directly
CLOUDFLARE_ACCOUNT_ID = os.environ['CF_ACCOUNT_ID']
GITHUB_REPO = 'rikkus/reponame'
PRODUCTION_BRANCH = 'main'  # or your default branch

# Optional: You can pass these as arguments instead.

headers = {
    "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "name": "srv-hemsley-cc",  # Project name, must be unique per account
    "production_branch": PRODUCTION_BRANCH,
    "source": {
        "type": "github",
        "config": {
            "owner": GITHUB_REPO.split('/')[0],
            "repo_name": GITHUB_REPO.split('/')[1],
            "production_branch": PRODUCTION_BRANCH
        }
    }
}

url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/pages/projects"

response = requests.post(url, json=data, headers=headers)
print(response.status_code, response.json())

import requests
from requests.auth import HTTPBasicAuth

# Jenkins credentials
JENKINS_URL = "http://localhost:8080"
JOB_NAME = "MS_AUTOMATION_1"  # Change this to your actual job name
USERNAME = "Ankit Sadavrati"
API_TOKEN = "asdfghjkl"  # Replace with your Jenkins API token

# Step 1: Get the CSRF Crumb
crumb_url = f"{JENKINS_URL}/crumbIssuer/api/json"
auth = HTTPBasicAuth(USERNAME, API_TOKEN)
crumb_response = requests.get(crumb_url, auth=auth)

if crumb_response.status_code == 200:
    crumb_data = crumb_response.json()
    crumb_value = crumb_data["crumb"]
    crumb_field = crumb_data["crumbRequestField"]  # This should be "Jenkins-Crumb"

    # Step 2: Trigger the Jenkins job with the Crumb included
    build_url = f"{JENKINS_URL}/job/{JOB_NAME}/build"
    headers = {crumb_field: crumb_value}  # Dynamic header field
    response = requests.post(build_url, auth=auth, headers=headers)

    if response.status_code == 201:
        print(f"✅ Jenkins Job '{JOB_NAME}' triggered successfully!")
    else:
        print(f"❌ Failed to trigger job. Status Code: {response.status_code}, Response: {response.text}")
else:
    print(f"❌ Failed to get Jenkins Crumb. Status Code: {crumb_response.status_code}, Response: {crumb_response.text}")

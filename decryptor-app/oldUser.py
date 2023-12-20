import requests
from barcodeAlgorithm import allBarcode
from barcodeAlgorithm import barcodeAlgorithm

BASE_URL = "https://generate-coding-challenge-server-rellb.ondigitalocean.app/"

def forgot_token(nuid):
    url = BASE_URL + f"forgot_token/{nuid}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text.strip() 
    else:
        print(f"Failed to retrieve token. Status code: {response.status_code}")
        return None

def get_challenge(token):
    url = BASE_URL + f"challenge/{token}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()["challenge"]
    else:
        print(f"Failed to retrieve challenge. Status code: {response.status_code}")
        return None

nuid = "002948556"
token = forgot_token(nuid)

def submit_solution(token, solution):
    url = BASE_URL + f"submit/{token}"
    data = solution

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to submit solution. Status code: {response.status_code}")
        return None

if token:
    print(f"Retrieved Token: {token}")

    challenge = get_challenge(token)

    if challenge:
        print(f"Retrieved Challenge: {challenge}")
        solution = allBarcode(challenge)


        submission_result = submit_solution(token, solution)

        if submission_result:
            print(f"Submission Result: {submission_result}")
            
    else:
        print("Failed to retrieve challenge. Unable to proceed with the challenge.")
else:
    print("Registration failed. Unable to proceed with the challenge.")

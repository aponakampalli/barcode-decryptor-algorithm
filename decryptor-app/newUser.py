import requests
from barcodeAlgorithm import allBarcode
from barcodeAlgorithm import barcodeAlgorithm

BASE_URL = "https://generate-coding-challenge-server-rellb.ondigitalocean.app/"

def register_user(name, nuid):
    url = BASE_URL + "register"
    data = {"name": name, "nuid": str(nuid)}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to register. Status code: {response.status_code}")
        return None

name = "Adithi Ponakampalli"
nuid = "002948556"

registration_data = register_user(name, nuid)

if registration_data:
    token = registration_data["token"]
    challenge = registration_data["challenge"]

    print(f"Token: {token}")
    print(f"Challenge: {challenge}")

    solution = allBarcode(challenge)

    def submit_solution(token, solution):
        url = BASE_URL + f"submit/{token}"
        data = solution

        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to submit solution. Status code: {response.status_code}")
            return None

    submission_result = submit_solution(token, solution)

    if submission_result:
        correct = submission_result["correct"]
        response_message = submission_result["response"]

        print(f"Submission Result: {response_message}")
        if correct:
            print("Congratulations! Your solution is correct.")
        else:
            print("Sorry, your solution is incorrect.")
else:
    print("Registration failed. Unable to proceed with the challenge.")
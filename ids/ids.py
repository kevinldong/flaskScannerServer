import requests

def virustotal_file_scan(file: str):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": open(file, "rb")}
    headers = {
        "Accept": "application/json",
        "x-apikey": 'api key',
        "Content-Type": "multipart/form-data"
    }

    response = requests.post(url, headers=headers)

    if response.text == 200:
        return True
    elif response.text == 400:
        return False

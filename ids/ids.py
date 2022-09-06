import requests

def virustotal_file_scan(file: str):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": open(file, "rb")}
    headers = {
        "Accept": "application/json",
        "x-apikey": '62f38e8e1c83d0c31ddaf4e93cc260c9e0aaaba9c72b949e4492d3e3a71c4a79',
        "Content-Type": "multipart/form-data"
    }

    response = requests.post(url, headers=headers)

    if response.text == 200:
        return True
    elif response.text == 400:
        return False

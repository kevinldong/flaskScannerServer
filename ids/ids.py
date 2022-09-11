import vt

def virustotal_file_scan(file: str):
    client = vt.Client("<API key>")
    files = {"file": open(file, "rb")}

    with open(files, "rb") as f:
        analysis = client.scan_file(f, wait_for_completion=True)

    if analysis == 200:
        return True
    else:
        return False

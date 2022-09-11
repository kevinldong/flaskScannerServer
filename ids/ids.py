import vt

def virustotal_file_scan(file: str):
    client = vt.Client("<62f38e8e1c83d0c31ddaf4e93cc260c9e0aaaba9c72b949e4492d3e3a71c4a79>")
    files = {"file": open(file, "rb")}

    with open(files, "rb") as f:
        analysis = client.scan_file(f, wait_for_completion=True)

    if analysis == 200:
        return True
    else:
        return False

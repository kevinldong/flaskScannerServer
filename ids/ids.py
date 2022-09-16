import vt
from io import BufferedReader


def virustotal_file_scan(file: str):
    client = vt.Client("API KEY")
    scan_file = BufferedReader(file)
    analysis = client.scan_file(scan_file, wait_for_completion=True)

    suspicious_count = analysis.stats['suspicious']
    malicious_count = analysis.stats['malicious']

    client.close()

    print("suspicious count = " + str(suspicious_count))
    print(f'{malicious_count=}')

    if suspicious_count > 5:
        return False
    elif malicious_count > 2:
        return False
    else:
        return True

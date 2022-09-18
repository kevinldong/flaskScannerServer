import vt
from io import BytesIO


def virustotal_file_scan(file: str):
    client = vt.Client("API KEY")
def virustotal_file_scan(file: str):
    client = vt.Client("gfeskmio")

    # Scan file
    analysis = client.scan_file(BytesIO(file), wait_for_completion=True)

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

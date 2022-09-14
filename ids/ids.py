import vt
from io import BufferedReader

def virustotal_file_scan(file: str):
    client = vt.Client("<API KEY>")

    # Wrap file in a BufferedReader to pass the API type check
    scan_file = BufferedReader(file)

    # Scan file
    analysis = client.scan_file(scan_file, wait_for_completion=True)

    # Get detection stats
    undetected_count = analysis.stats['undetected']
    harmless_count = analysis.stats['harmless']
    suspicious_count = analysis.stats['suspicious']
    malicious_count = analysis.stats['malicious']

    # Get completion status
    completion = analysis.status

    # TODO: use above to make decision of whether to save
    while completion == 'completed':
        if undetected_count == 0:
            return False
        elif harmless_count == 0:
            return False
        elif suspicious_count > 0:
            return False
        elif malicious_count > 0:
            return False
        else:
            return True

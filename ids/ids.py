"""
Module to provide IDS functionality for our Flask webserver

"""

def virustotal_file_scan(file: str) -> bool:
    """Function to scan a file with the VT API

    Args:
        file: a str containing the contents of the file to save
    Returns:
        a bool indicating whether the file is safe to save
    """
    raise NotImplementedError
    return False

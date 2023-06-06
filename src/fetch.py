import re
import requests
import os
import sys

def main():
    args = sys.argv
    if len(args) < 2:
        print("Too few arguments, at least one required")
        return

    print("Get url:", args[1])
    response = requests.get(args[1])
    if response.status_code != 200:
        print("Could not fetch file")
        return

    body = response.text
    print("Get data:", len(body), "bytes")

    pattern = r"download: \[.*?\]\((https?://.*?)\)"
    regex = re.compile(pattern)
    matches = regex.findall(body)
    for match in matches:
        url = match
        file_name = os.path.basename(url)

        print("Get image:", file_name, "\n\turl:", url)
        if download_file(url, file_name):
            print("Download successful")
        else:
            print("Download failed!")

def download_file(url, path):
    response = requests.get(url)
    if response.status_code != 200:
        return False

    with open(path, 'wb') as file:
        file.write(response.content)

    return True

if __name__ == "__main__":
    main()

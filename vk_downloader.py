import argparse
import json
import os
from urllib.request import urlretrieve

from haralyzer import HarParser


def save_file_system(url, folder, filename):
    """Saves the file from the given URL to the specified folder.

    Args:
        url (str): The URL of the file to download.
        folder (str): The path to the folder where the file will be saved.
        filename (str): The name of the saved file.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    urlretrieve(url, folder + "/" + filename)


def process_har_file(har_file_path):
    """Processes a HAR file and downloads images.

    Args:
        har_file_path (str): The path to the HAR file.
    """
    with open(har_file_path, 'r', encoding='utf-8') as f:
        har_parser = HarParser(json.loads(f.read()))

        for entry in har_parser.har_data['entries']:
            if entry['request']:
                url: str = entry['request']['url']
                headers = entry['response']['headers']
                if url.__contains__(".jpg?size"):
                    for item in headers:
                        if item['name'] == "date":
                            file_name = url.split("/")[-1].split("?")[0].replace(".jpg", item[
                                'value'] + ".jpg").replace(" ", "_")
                            print(file_name)
                            save_file_system(url, "photos", file_name)
                            print(url)
                        else:
                            continue


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Processes a HAR file and downloads images')
    parser.add_argument('har_file', help='Path to the HAR file to process')
    args = parser.parse_args()

    # Process the HAR file
    process_har_file(args.har_file)

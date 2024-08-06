import json
import os
from urllib.request import urlretrieve

from haralyzer import HarParser


def save_file_system(url, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    urlretrieve(url, folder + "/" + filename)


with open('vk.com.har', 'r', encoding='utf-8') as f:
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

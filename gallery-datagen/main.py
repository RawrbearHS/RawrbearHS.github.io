import requests
import json
import os
from datetime import datetime
from PIL import Image


def ordinal(n):
    return str(n)+("th" if 4<=n%100<=20 else {1:"st",2:"nd",3:"rd"}.get(n%10, "th"))


def main():
    # ids = get_data_from_file()
    # download_data(ids)
    # download_thumbnails()
    process_datafiles()

def download_thumbnails():
    path = os.path.join(os.getcwd(), "projects")
    for filename in os.listdir(path):
        try:
            with open(os.path.join(path, filename), 'r') as f:
                data = json.load(f)
                img_response = requests.get(data["screenshot_url"])
                if img_response.status_code == 200:
                    imgpath = os.path.join(path, "thumbnails/", f"{data["uuid"]}.png")
                    with open(imgpath, 'wb') as imgfile:
                        imgfile.write(img_response.content)
        except IsADirectoryError:
            pass

def process_datafiles():
    out = ""
    path = os.path.join(os.getcwd(), "projects")
    for filename in os.listdir(path):
        try:
            with open(os.path.join(path, filename), 'r') as f:
                data = json.load(f)
                template_data = {
                    "name": data["title"],
                    "href": f"https://c.gethopscotch.com/p/{data["uuid"]}",
                    "img": f"/img/gallery/{data["uuid"]}.png",
                    # Convert date from XXXX-XX-XX to a neater format
                    "date":
                        datetime.strptime(data["correct_published_at"].split("T")[0], "%Y-%m-%d")
                            .strftime("%B %d, %Y"),
                    "likes": data["number_of_stars"],
                    "plays": data["play_count"],
                }
                thumbnail = Image.open(os.path.join(path, "thumbnails", f"{data["uuid"]}.png"))
                width, height = thumbnail.size
                if width != height: template_data["wide"] = True
                thumbnail.close()
                out += ("{{ comp.project(" + json.dumps(template_data) + ") }}".strip())
                out += "\n"
        except IsADirectoryError:
            pass
    with open(os.path.join(os.getcwd(), "projects", "templates.vto"), "w") as f:
        f.write(out)

def get_data_from_file():
    ids = []
    with open('project_list.txt', 'r') as file:
        for line in file:
            if "/p/" in line:
                ids.append(line.strip().split("/p/")[1])
    return ids

def download_data(ids):
    for id in ids:
        response = json.loads(requests.get(f"http://community.gethopscotch.com/api/v1/projects/{id}").text)
        with open(f"projects/{response["title"]}.json", 'w') as file:
            json.dump(response, file)

if __name__ == "__main__":
    # download_data(["11k4wuoq1p"])
    main()

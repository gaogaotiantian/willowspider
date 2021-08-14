import re
import requests
import sys


def get_all_status(s):
    status = re.findall(r"<a.*?data-floorplan-name.*?>\s*(.*?)\s*</a>", s, re.MULTILINE)
    status = [st for st in status if "Video" not in st]
    return status


if __name__ == "__main__":
    r = requests.get("https://www.willowspringsapartments.com/floorplans")

    if r.status_code != 200:
        print("Fail to get data")
        sys.exit(1)

    status = get_all_status(r.text)
    print(status)
    if any((st != "Contact Us" for st in status)):
        print("Found availability")
        sys.exit(1)

import requests
from bs4 import BeautifulSoup
import json
import os
import re

USERNAME = "Shreya3501"

url = f"https://github.com/users/{USERNAME}/contributions"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

if response.status_code != 200:
    print("Failed to fetch contributions.")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

days = []

cells = soup.find_all("td", class_="ContributionCalendar-day")

for cell in cells:

    tooltip = cell.find_next("tool-tip")

    count = 0

    if tooltip:
        text = tooltip.text.strip()

        if "No contributions" not in text:
            m = re.search(r"(\d+)", text)
            if m:
                count = int(m.group(1))

    days.append({
        "date": cell.get("data-date"),
        "count": count,
        "level": int(cell.get("data-level", 0))
    })

os.makedirs("data", exist_ok=True)

with open("data/contributions.json", "w") as f:
    json.dump(days, f, indent=4)

print(f"Saved {len(days)} contribution days.")
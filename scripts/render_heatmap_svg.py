import json

with open("data/contributions.json") as f:
    days = json.load(f)

CELL = 12
GAP = 3

PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353"
]

weeks = []

for i in range(0, len(days), 7):
    weeks.append(days[i:i+7])

svg = []

WIDTH = len(weeks) * (CELL + GAP) + 40
HEIGHT = 7 * (CELL + GAP) + 70

svg.append(f'''
<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">
''')

svg.append('''
<rect width="100%" height="100%" fill="#0d1117"/>
''')

for x, week in enumerate(weeks):

    for y, day in enumerate(week):

        color = PALETTE[min(day["level"], 4)]

        svg.append(f'''
<rect
x="{25 + x*(CELL+GAP)}"
y="{20 + y*(CELL+GAP)}"
width="{CELL}"
height="{CELL}"
rx="3"
fill="{color}">

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.3s"
begin="{(x+y)*0.02}s"
fill="freeze"/>

</rect>
''')

svg.append("</svg>")

with open("contrib-heatmap.svg", "w") as f:
    f.write("\n".join(svg))

print("contrib-heatmap.svg created!")
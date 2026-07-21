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



svg = []

svg.append(f'''
<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" fill="#0d1117">

<animate
attributeName="opacity"
from="0"
to="1"
dur="0.5s"
fill="freeze"/>

</rect>

<defs>

<filter id="glow">

<feDropShadow
dx="0"
dy="0"
stdDeviation="2"
flood-color="#39d353"/>

</filter>

</defs>
''')

svg.append('''
<g>

<animateTransform
attributeName="transform"
type="translate"
values="0 25;0 0"
dur="0.8s"
fill="freeze"/>

<animate
attributeName="opacity"
values="0;1"
dur="0.8s"
fill="freeze"/>
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
fill="{color}"
filter="url(#glow)">

<animate
attributeName="opacity"
values="0;1"
dur="0.4s"
begin="{x*0.08+y*0.03}s"
fill="freeze"/>

<animateTransform
attributeName="transform"
type="scale"
values="0;1"
begin="{x*0.08+y*0.03}s"
dur="0.4s"
fill="freeze"/>

<animate
attributeName="opacity"
values="1;0.8;1"
begin="{x*0.08+y*0.03+0.6}s"
dur="2s"
repeatCount="indefinite"/>

</rect>
''')

svg.append("</g>")
svg.append("</svg>")

with open("contrib-heatmap.svg", "w") as f:
    f.write("\n".join(svg))

print("contrib-heatmap.svg created!")
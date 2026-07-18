INFO = [
    ("Name", "Shreya Sunal"),
    ("Role", "B.Tech CSE Student"),
    ("College", "Graphic Era Hill University"),
    ("Languages", "C, C++, Python, Java"),
    ("Frontend", "HTML, CSS, JS, React"),
    ("Backend", "Node.js, Express.js"),
    ("Database", "MongoDB, MySQL"),
    ("Focus", "DSA | Web Development"),
    ("GitHub", "github.com/Shreya3501")
]

WIDTH = 650
HEIGHT = 320

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">

<rect width="100%" height="100%" rx="15" fill="#0d1117"/>

<text x="25" y="35"
font-family="Courier New"
font-size="24"
fill="#58a6ff">
My Info Card
</text>
'''

y = 70

for key, value in INFO:
    svg += f'''
<text x="25"
      y="{y}"
      font-family="Courier New"
      font-size="16"
      fill="#d1d5db">
{key:<12}: {value}
</text>
'''
    y += 28

svg += "</svg>"

with open("info-card.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("info-card.svg created!")
from PIL import Image, ImageEnhance, ImageFilter

# -----------------------------
# Settings
# -----------------------------
IMAGE = "source-prepped.png"
OUTPUT = "avi-ascii.svg"

WIDTH = 80
FONT_SIZE = 11
LINE_HEIGHT = 13

# Dark -> Light
ASCII = "@%#*+=-:. "

# -----------------------------
# Load Image
# -----------------------------
img = Image.open(IMAGE).convert("L")

# Increase contrast
img = ImageEnhance.Contrast(img).enhance(2.0)

# Sharpen image
img = img.filter(ImageFilter.SHARPEN)

# Resize while keeping aspect ratio
w, h = img.size
aspect = h / w

HEIGHT = int(aspect * WIDTH * 0.55)

img = img.resize((WIDTH, HEIGHT))

pixels = img.load()

rows = []

for y in range(HEIGHT):
    line = ""

    for x in range(WIDTH):

        p = pixels[x, y]

        # Ignore almost-white background
        if p > 245:
            line += " "
            continue

        idx = int((255 - p) / 255 * (len(ASCII) - 1))
        line += ASCII[idx]

    rows.append(line)
    # -----------------------------
# Build SVG
# -----------------------------

svg = []

svg.append(f'''
<svg xmlns="http://www.w3.org/2000/svg"
width="900"
height="{HEIGHT*LINE_HEIGHT+60}"
viewBox="0 0 900 {HEIGHT*LINE_HEIGHT+60}">
''')

svg.append('''
<rect width="100%" height="100%" fill="#0d1117"/>
''')

x = 40
y = 40

for row in rows:

    svg.append(f'''
<text
x="{x}"
y="{y}"
font-family="Courier New, monospace"
font-size="{FONT_SIZE}"
fill="#d1d5db"
xml:space="preserve">{row}</text>
''')

    y += LINE_HEIGHT

svg.append("</svg>")

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write("\n".join(svg))

print("SVG Created Successfully!")
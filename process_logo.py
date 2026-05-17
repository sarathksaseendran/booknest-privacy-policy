from PIL import Image
import collections

# Open the image
img = Image.open('logo/app_logo.png').convert("RGBA")
pixels = img.load()
width, height = img.size

# Get top-left pixel as background color
bg_color = pixels[0, 0]

# Keep track of colors for dominant color (excluding bg_color and transparent)
colors = []

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x, y]
        # Make background color transparent
        # Using a small threshold in case of compression artifacts
        if abs(r - bg_color[0]) < 15 and abs(g - bg_color[1]) < 15 and abs(b - bg_color[2]) < 15:
            pixels[x, y] = (r, g, b, 0)
        elif a > 0:
            colors.append((r, g, b))

# Find the most common colors
counter = collections.Counter(colors)
most_common = counter.most_common(5)

print("Background color:", bg_color)
print("Dominant colors:")
for color, count in most_common:
    print(f"#{color[0]:02x}{color[1]:02x}{color[2]:02x} - Count: {count}")

# Save the image
img.save('logo/app_logo.png')
print("Image saved with transparent background.")

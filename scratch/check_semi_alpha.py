from PIL import Image

im = Image.open('assets/images/boloupgoagency-nobg.png')
print("Image size:", im.size)

# Check edges for semi-transparent non-zero alpha
# Let's check along the 4 borders
top_row = [im.getpixel((x, 5))[3] for x in range(0, im.width, 20)]
bottom_row = [im.getpixel((x, im.height - 5))[3] for x in range(0, im.width, 20)]
left_col = [im.getpixel((5, y))[3] for y in range(0, im.height, 20)]
right_col = [im.getpixel((im.width - 5, y))[3] for y in range(0, im.height, 20)]

print("Top row alphas (sampled):", max(top_row), "avg:", sum(top_row)/len(top_row))
print("Bottom row alphas (sampled):", max(bottom_row), "avg:", sum(bottom_row)/len(bottom_row))
print("Left col alphas (sampled):", max(left_col), "avg:", sum(left_col)/len(left_col))
print("Right col alphas (sampled):", max(right_col), "avg:", sum(right_col)/len(right_col))

# Let's sample a grid to see where alpha is > 0
for y in range(0, im.height, 150):
    line = "".join(["#" if im.getpixel((x, y))[3] > 10 else " " for x in range(0, im.width, 20)])
    print(f"y={y:4d} |{line}|")


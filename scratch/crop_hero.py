from PIL import Image

im = Image.open('.playwright-mcp/page-2026-11-07T08-27-08-818Z.png')
print('Screenshot size:', im.size)
# Save hero crop
hero_crop = im.crop((im.width//2, 80, im.width, 700))
hero_crop.save('scratch/hero_crop_live.png')
print('Saved scratch/hero_crop_live.png')


from PIL import Image

im = Image.open('.playwright-mcp/page-2026-11-07T08-36-23-350Z.png')
print('Screenshot size:', im.size)
hero_crop = im.crop((im.width//2, 80, im.width, 674))
hero_crop.save('scratch/hero_crop_after_deploy.png')
print('Saved scratch/hero_crop_after_deploy.png')


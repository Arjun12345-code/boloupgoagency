from PIL import Image

im = Image.open('assets/images/boloup-agent-role.png')
print("Size:", im.size, "Mode:", im.mode)
# let's save a thumb to inspect
im.thumbnail((400, 250))
im.save('scratch/agent_role_thumb.png')
print("Saved scratch/agent_role_thumb.png")


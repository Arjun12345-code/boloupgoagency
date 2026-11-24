def update_style():
    with open('style.css', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .reg-step-media
    old_media = '''.reg-step-media {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  border: 1.5px solid rgba(255, 69, 0, 0.4);
  background: radial-gradient(ellipse at 50% 25%, rgba(18, 27, 42, 0.6) 0%, rgba(8, 12, 20, 0.95) 100%);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.6),
    0 0 32px rgba(255, 69, 0, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  width: 100%;
  max-width: 580px;
  padding: 12px;
  margin: 0 auto;
  perspective: 1100px;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.5s ease;
  cursor: zoom-in;
}'''

    new_media = '''.reg-step-media {
  position: relative;
  border-radius: 20px;
  overflow: hidden;
  border: 1.5px solid rgba(255, 69, 0, 0.4);
  background: radial-gradient(ellipse at 50% 25%, rgba(18, 27, 42, 0.6) 0%, rgba(8, 12, 20, 0.95) 100%);
  box-shadow: 
    0 16px 36px rgba(0, 0, 0, 0.55),
    0 0 24px rgba(255, 69, 0, 0.18),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  width: 100%;
  max-width: 280px;
  padding: 8px;
  margin: 16px auto 0;
  perspective: 1100px;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.5s ease;
  cursor: zoom-in;
}'''

    assert old_media in content, "old_media not found in style.css"
    content = content.replace(old_media, new_media)

    # 2. Update .reg-step-media img
    old_img = '''.reg-step-media img {
  width: 100%;
  height: auto;
  object-fit: cover;
  display: block;
  border-radius: 14px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
}'''

    new_img = '''.reg-step-media img {
  width: 100%;
  height: auto;
  max-height: 480px;
  object-fit: contain;
  display: block;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
}'''

    assert old_img in content, "old_img not found in style.css"
    content = content.replace(old_img, new_img)

    # 3. Update mobile media query
    old_mob = '''  .reg-step-media {
    max-width: 100%;
    padding: 8px;
    border-radius: 16px;
  }'''

    new_mob = '''  .reg-step-media {
    max-width: 240px;
    padding: 6px;
    border-radius: 16px;
    margin: 14px auto 0;
  }'''

    assert old_mob in content, "old_mob not found in style.css"
    content = content.replace(old_mob, new_mob)

    # 4. Remove .agency-id-code from mobile query
    old_mob_id = '''  .agency-id-code {
    font-size: 1.6rem;
  }
'''
    if old_mob_id in content:
        content = content.replace(old_mob_id, '')

    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(content)
    print("style.css updated successfully!")

if __name__ == '__main__':
    update_style()


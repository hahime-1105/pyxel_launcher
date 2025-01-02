from PIL import Image, ImageOps

img_file = 'C:\\Users\\user\\Downloads\\トウコ_立ち絵.png'

img_bef = Image.open(img_file)

(width, height) = (img_bef.width // 2, img_bef.height // 2)
img_aft = img_bef.resize((48, 48))
img_aft.save('C:\\Users\\user\\Downloads\\トウコ_立ち絵2.png')

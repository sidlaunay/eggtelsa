from PIL import Image

img_file = r'C:\Users\s.launay\Downloads\4872173-removebg-preview.png'
img = Image.open(img_file)
img.save('icon.ico',format = 'ICO', sizes = [(256,256)])

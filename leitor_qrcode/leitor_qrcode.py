# instalar as libs
# pip install Pillow
# pip install pyzbar

from PIL import Image
from pyzbar.pyzbar import decode

read = decode(Image.open('QRCode.png'))
print(read[0].data)

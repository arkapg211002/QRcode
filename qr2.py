import qrcode
img = qrcode.img('Some data here')
type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")
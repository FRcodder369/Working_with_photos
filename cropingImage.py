from PIL import Image

def crop_Image(path, cropped_path, sizes):
    image = Image.open(path)
    cropped = image.crop(*sizes)
    cropped.save(cropped_path)


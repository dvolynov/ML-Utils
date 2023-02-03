from PIL import Image


def smart_trimming(img, size=(100, 100)):

    # In height
    if img.width < size[0]:
        new_height = int(size[0] * img.height / img.width)
        img = img.resize((size[0], new_height), Image.ANTIALIAS)

    # In width
    if img.height < size[1]:
        new_width = int(img.width * size[1] / img.height)
        img = img.resize((new_width, size[1]), Image.ANTIALIAS)

    # Reducing large
    if img.width > size[0] and img.height > size[1]:

        # In height
        if img.width > img.height:
            new_height = int(size[0] * img.height / img.width)
            img = img.resize((size[0], new_height), Image.ANTIALIAS)
        else:
            # In width
            new_width = int(img.width * size[1] / img.height)
            img = img.resize((new_width, size[1]), Image.ANTIALIAS)

    # Creating a new image
    new_img = Image.new("RGB", size, (255, 255, 255))

    # Defining box by center
    left = (size[0] - img.width) // 2
    top = (size[1] - img.height) // 2

    # Pasting box on new image
    new_img.paste(img, (left, top))

    return new_img
from PIL import Image


def smart_trimming(img, target_size):
    if img.width < target_size[0]:
        new_height = int(target_size[0] * img.height / img.width)
        img = img.resize((target_size[0], new_height), Image.ANTIALIAS)

    if img.height < target_size[1]:
        new_width = int(img.width * target_size[1] / img.height)
        img = img.resize((new_width, target_size[1]), Image.ANTIALIAS)

    new_img = Image.new("RGB", target_size, (255, 255, 255))

    left = (target_size[0] - img.width) // 2
    top = (target_size[1] - img.height) // 2

    new_img.paste(img, (left, top))

    return new_img
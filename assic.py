from PIL import Image

# change filename if needed
IMAGE_PATH = "dragon.png"

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=120):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join(ASCII_CHARS[pixel // 25] for pixel in pixels)

def main():
    image = Image.open(IMAGE_PATH)
    image = resize_image(image)
    image = grayify(image)

    ascii_str = pixels_to_ascii(image)
    width = image.width

    ascii_img = "\n".join(
        ascii_str[i:(i+width)]
        for i in range(0, len(ascii_str), width)
    )

    print(ascii_img)

if __name__ == "__main__":
    main()

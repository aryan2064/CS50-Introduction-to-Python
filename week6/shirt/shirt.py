import sys

from PIL import Image, ImageOps
from os.path import splitext


SHIRT_FILEPATH = "shirt.png"


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_filepath = sys.argv[1].lower()
    output_filepath = sys.argv[2].lower()

    if splitext(input_filepath)[1] not in (".png", ".jpg", ".jpeg"):
        sys.exit("Invalid input")

    if splitext(output_filepath)[1] not in (".png", ".jpg", ".jpeg"):
        sys.exit("Invalid output")

    if splitext(input_filepath)[1] != splitext(output_filepath)[1]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_filepath) as input_image, Image.open(
            SHIRT_FILEPATH
        ) as shirt_image:
            shirt_size = shirt_image.size

            # Scales input_image to fit shirt_image dimensions, keeping its aspect ratio
            output_image = ImageOps.fit(input_image, shirt_size)

            # The second shirt_image is a mask, in order for the non-transparent pixels to be used
            output_image.paste(shirt_image, shirt_image)

            output_image.save(output_filepath)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

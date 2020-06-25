"""
Program 9.10
Create a New Image from an Existing Image
"""


def main():
    with open("Chapter09/archean.png", "rb") as existing_image, open("Chapter09/new_archean.png", "wb") as new_image:
        for each_line_bytes in existing_image:
            new_image.write(each_line_bytes)


if __name__ == "__main__":
    main()

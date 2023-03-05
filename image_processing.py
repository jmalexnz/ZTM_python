from PIL import Image, ImageFilter
# Look into openCV as well for exploring

def image_playground():
    img = Image.open("./Pokedex/pikachu.jpeg")
    print(img.format)
    print(img.size)
    print(img.mode)

    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save("blur.png", 'png')
    filtered_img = img.filter(ImageFilter.SMOOTH)
    filtered_img.save("smooth.png", 'png')
    # Can convert images to different formats
    # e.g., greyscale
    # filtered_img.show()
    filtered_img = filtered_img.rotate(90)
    filtered_img = filtered_img.convert('L')
    filtered_img = filtered_img.resize((300, 300))
    # use thumbnail to resize while maintaining aspect ratio.
    filtered_img.show()

    # use the pillow documentation to help

import sys
import os
import glob

def JPGtoPNGconverter(image_folder, output_folder):
    '''
    Convert image files in folder to a jpg
    and save 
    '''
    # check if new folder exists, if not create
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # loop through files in folder
    # convert images to png and save to new folder
    for image_file in os.listdir(image_folder):
        img = Image.open(f'{image_folder}{image_file}')
        clean_name = os.path.splitext(image_file)
        img.save(f'{output_folder}{clean_name[0]}.png', 'png')

def main():
    '''
    Main function
    '''
    # print(len(sys.argv))
    JPGtoPNGconverter(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
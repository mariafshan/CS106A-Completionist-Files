# import the MemeGenerator class from memegen.py
from memegenerator import MemeGenerator
from simpleimage import SimpleImage

def main():
    # initalize the meme generator with an image
    meme_gen = MemeGenerator('spongebob-imagination.jpg')

    # add text to the top and bottom of the meme
    meme_gen.add_text('CODING IN C', 175, 40)
    meme_gen.add_text('THAT LOOKS SIMPLE', 120, 275)

    # generate the meme!
    meme_gen.render()

if __name__ == '__main__':
    main()

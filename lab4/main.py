from utils import *


if __name__ == "__main__":
    c = scaleImage('data/1.jpg')
    operationOnImage(c, 'addition')
    operationOnImage(c, 'subtraction')
    operationOnImage(c, 'division')
    operationOnImage(c, 'multiplication')
    operationOnImage(c, 'special')
    operationOnImage(c, 'black&white')
    operationOnImage(c, 'rgb')

    equalizeImage(c)
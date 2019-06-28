import os
import argparse
from datetime import datetime
from PIL import Image


parser = argparse.ArgumentParser(description="Process some image")
parser.add_argument('path' , help='The path to the image you\'d like to resize')
parser.add_argument('NewWidth', type=int , help='The new width you\'d like the image to be')
parser.add_argument('NewHeight', type=int, help='The new height you\'d like the image to be')
parser.add_argument('-O',  '--overwrite', type=bool, default=False, help='Causes script to overwrite the original image (out parameter will be ignored if set)')
parser.add_argument('-o','--out', help="Set a custom output path")


args = parser.parse_args()

print(args)

def CreateNewFilePath(filepath):
    basename = os.path.basename(filepath) 
    directory = os.path.split(filepath)[0]
    seperator = '.'

    file = basename.split('.')
    file[0] += str.format("({0})[{1}x{2}]", datetime.now().strftime("%y%m%d%H%M%S") , args.NewWidth , args.NewHeight) 
    basename = seperator.join(file)


    return directory + "/" +  basename


if os.path.exists(args.path):

    basename = os.path.basename(args.path)
    directory = (os.path.split(args.path))[1]
    image = Image.open( args.path )
    print( "Image coming from {1}" , directory)
    print ( str.format("{0} was:  {1} x {2}" , basename, image.size[0] , image.size[1])  )

    image = image.resize( (args.NewWidth, args.NewHeight) )

    print ( str.format("Image is now: {0}" ,  image.size.__str__())  )

    if args.overwrite:
        NewFile = args.path

    elif args.out != None:
        NewFile = args.out 

    else:
        NewFile = CreateNewFilePath(args.path)

    print(str.format("Saving image to {0}", NewFile))
    image.save(NewFile)
    image.close()
else:
    print ( "Incorrect path!")



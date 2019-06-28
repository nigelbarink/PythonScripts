# PythonScripts
Helper scripts for common task in python


- image-resize.py
      usage: image-resize.py [-h] [-O OVERWRITE] [-o OUT] path NewWidth NewHeight

      Process some image

      positional arguments:
        path                  The path to the image you'd like to resize
        NewWidth              The new width you'd like the image to be
        NewHeight             The new height you'd like the image to be

      optional arguments:
        -h, --help            show this help message and exit
        -O OVERWRITE, --overwrite OVERWRITE
                              Causes script to overwrite the original image (out
                              parameter will be ignored if set)
        -o OUT, --out OUT     Set a custom output path

#notesFromPaper
Year   :
Tags   : [[image labeling]]
Authors: [[Yu]] [[Wu]] [[Luo]] [[Ren]]

Do you have an image set for machine learning? Flip and rotate it for more data. Bing bang boom

```
from PIL import Image
TRANSFORMS = {
        "identity":   lambda im: im,
        "rot90":      lambda im: im.transpose(Image.ROTATE_90),
        "rot180":     lambda im: im.transpose(Image.ROTATE_180),
        "rot270":     lambda im: im.transpose(Image.ROTATE_270),
        "flip":       lambda im: im.transpose(Image.FLIP_LEFT_RIGHT),
        "rot90flip":  lambda im: im.transpose(Image.ROTATE_90).transpose(Image.FLIP_LEFT_RIGHT),
        "rot180flip": lambda im: im.transpose(Image.ROTATE_180).transpose(Image.FLIP_LEFT_RIGHT),
        "rot270flip": lambda im: im.transpose(Image.ROTATE_270).transpose(Image.FLIP_LEFT_RIGHT)}
```

             #Note: For proper result just take large images
from PIL import Image
import os

#create image specific object which provides us so many methods for image manipulation
for f in os.listdir('images'):
    if f.endswith('.jpg'):  # in my case i took only .jpg format image, you can take as you wish :)
        image=Image.open('images/{}'.format(f))
        #Creating copy of that image for safety
        image.copy()
        size=(1280,720)

        fname,fexten=os.path.splitext(f)

        if not os.path.exists('thumbnail images'):
            os.mkdir('thumbnail images')

        image.thumbnail(size)
        image.save('thumbnail images/{}{}'.format(fname,fexten))




# meme-recycler

Reformats a directory of memes.

This project uses code from three previous projects:

1. [meme-cropper](https://github.com/evmarts/meme-cropper) to partition input memes into two images; an image of the text and a meme pic image.
2. [meme-text-ocr](https://github.com/evmarts/meme-text-ocr) to recognize the text from the image of text as a string.
3. [meme-maker](https://github.com/evmarts/meme-maker) to create a meme.

### Motivation:

Memes can come in all shapes and sizes: 

<img src="./figs/old_memes.jpg" width="1080px" alt="">

But sometimes it is nice to keep a simple format:

<img src="./figs/new_memes.jpg" width="1080px" alt="">

### meme-recycler.py

1.
Crops the meme into its two components:

~~~
$ python meme-recycler.py
Cropping images...
cropped meme0.jpg
cropped meme1.jpg
cropped meme2.jpg
~~~

text components:

<img src="./figs/meme0_text.jpg" width="200" alt=""><img src="./figs/meme1_text.jpg" width="200" alt=""><img src="./figs/meme2_text.jpg" width="200" alt="">

pic components:

<img src="./figs/meme0_pic.jpg" width="200" alt=""><img src="./figs/meme1_pic.jpg" width="200" alt=""><img src="./figs/meme2_pic.jpg" width="200" alt="">

2.
Reconizes the text component as a string:

~~~
Applying OCR on images of text...
Got text of meme0_text.jpg
Got text of meme1_text.jpg
Got text of meme2_text.jpg
~~~

3.
Creates new memes:

~~~
Constructing images...
Created new meme image: meme0.jpg
Created new meme image: meme1.jpg
Created new meme image: meme2.jpg
~~~

output images:

<img src="./figs/meme0.jpg" width="200" alt=""><img src="./figs/meme1.jpg" width="200" alt=""><img src="./figs/meme2.jpg" width="200" alt="">
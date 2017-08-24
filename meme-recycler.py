import os
from meme_cropper import meme_cropper_main
from meme_text_ocr import meme_text_ocr_main
from meme_maker import meme_maker_main


## returns true if the given path is of an image, false otherwise
def is_img(path):
	ext = path[-4:]
	if (ext == ".jpg") or (ext == ".png") or (ext == "jpeg"):
		return True
	return False

## crops all the recyclable memes into images of text and images of pics, storing
#  in '/text' and '/pic' directories respectively
def crop_memes(paths):
	print "Cropping images..."
	for path in paths:
		if is_img(path):
			meme_cropper_main("in/" + str(path))
			print "cropped " + str(path)
	return 0

## returns the paths of images inside the '/pic' directory
def get_pic_paths(files):
	pic_paths = []
	for file in files:
		if is_img(file):
			pic_paths.append(file)
	return pic_paths

## returns a list of strings corresponding to the text of the images in the '/text' 
#  directory
def get_texts(text_images):
	print "Applying OCR on images of text..."
	texts = []
	for text_image in text_images:
		if is_img(text_image):
			texts.append(meme_text_ocr_main("in/text/" + str(text_image)))
			print "Got text of " + str(text_image)
	return texts

## constructs new meme images
def make_memes(meme_tuples):
	print "Constructing images..."
	for meme_tuple in meme_tuples:
		meme_maker_main(meme_tuple[0], "../meme-recycler/in/pic/" + str(meme_tuple[1]))
		print "Created new meme image: " + str(meme_tuple[1]).replace("_pic","")
	print "Done!"

def main():
	paths = os.listdir("../meme-recycler/in")			
	crop_memes(paths)
	text_images = os.listdir("../meme-recycler/in/text")
	texts = get_texts(text_images)
	files = os.listdir("../meme-recycler/in/pic")
	pic_paths = get_pic_paths(files)
	meme_tuples = zip(texts, pic_paths)
	make_memes(meme_tuples)

main()
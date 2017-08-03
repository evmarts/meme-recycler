import os
from meme_cropper import meme_cropper_main
from meme_text_ocr import meme_text_ocr_main
from meme_maker import meme_maker_main

def is_jpg(path):
	ext = path[-4:]
	# print ext
	if (ext == ".jpg") or (ext == ".png") or (ext == "jpeg"):
		return True

paths = os.listdir("../meme-recycler/recyclable-memes")

for path in paths:
	if is_jpg(path):
		meme_cropper_main("recyclable-memes/" + str(path))

text_images = os.listdir("../meme-recycler/recyclable-memes/text")
# print text_images

texts = []
for text_image in text_images:
	if is_jpg(text_image):
		texts.append(meme_text_ocr_main("recyclable-memes/text/" + str(text_image)))

files = os.listdir("../meme-recycler/recyclable-memes/pic")

pic_images = []
for file in files:
	if is_jpg(file):
		pic_images.append(file)

meme_tuples = zip(texts, pic_images)

for meme_tuple in meme_tuples:
	meme_maker_main(meme_tuple[0], "../meme-recycler/recyclable-memes/pic/" + str(meme_tuple[1]))

# print text_images
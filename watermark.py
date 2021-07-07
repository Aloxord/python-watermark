#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os, errno, re, time
from PIL import Image, ImageDraw, ImageFont

PREFIX = "wm_"

dirs = list(filter(lambda x: x.find(PREFIX) and re.search(r'\.png',x) ,os.listdir()))

def process(file):

	logo = Image.open('wm_logo.png').convert('RGBA')
	image = Image.open(file).convert('RGBA')
	waterMark = Image.new('RGBA', image.size, (255,255,255,0))

	width = int(image.size[0])
	txt_w = 80

	height = int(image.size[1])
	txt_v = int(height / 10)
	
	logo = logo.resize((txt_w,txt_w))
	isPastable = True
	# draw = ImageDraw.Draw(txt)
	# font = ImageFont.truetype("KeepCalm-Medium.ttf", 12)
	for i in range(0, height, txt_w):
		for j in range(0, (width - txt_w), txt_w):
			# draw.text((j, i), "@BLABLABLA", font=font, fill=(255,255,255,20))
			if isPastable:
				waterMark.paste(logo,(j, i))

			isPastable = not isPastable

	newImage = Image.alpha_composite(image,waterMark)
	newImage.save(PREFIX+file)
	os.remove(file)

while 1:

	print('New dirs: ')
	for file in dirs:
		print(file)
		process(file)
	time.sleep(5)
	dirs = list(filter(lambda x: x.find(PREFIX) and re.search(r'\.png|\.jpg',x) ,os.listdir()))
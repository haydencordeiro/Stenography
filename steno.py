
from PIL import Image
import stepic
ask=int(input('1:encode,2:deocde'))
if(ask==1):
	im = Image.open(input('Enter File Name'))
	print(im)
	file2=input('enter name of file 2')
	text=input('enter text')
	im1 = stepic.encode(im, text.encode('utf-8'))
	im1.save(file2, 'PNG')

if(ask==2):
	im2 = Image.open(input('enter File name'))
	stegoImage = stepic.decode(im2)
	print(stegoImage)
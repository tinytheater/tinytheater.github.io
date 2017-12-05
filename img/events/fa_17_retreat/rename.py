import os

i = 0
names = os.listdir()
names.sort()
for filename in names:
	if "JPG" in filename or "jpg" in filename:
		newname = "%s.jpg" % i
		os.rename(filename, newname)
		i += 1
		print('<div class="item">')
		print('    <img src="../../img/events/fa_17_anniversary/' + newname + '" width="100%">')
		print('</div>')

import os

def rename_files():
	path = os.listdir(r"Downloads/prank")
	#print path
	origin_path = os.getcwd()
	print "current dir "+ origin_path
	#print 
	os.chdir(r"Downloads/prank") 
	for name in path:
		print name
		os.rename(name, name.translate(None, "0123456789"))
		print name
rename_files()

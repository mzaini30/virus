import time, os

while True:
	os.system("git status")
	os.system("git add -A .")
	os.system("git commit -m 'oke'")
	os.system("git push")
	print
	time.sleep(180)
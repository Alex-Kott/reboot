import subprocess
import time
import re

file_path = "file.txt"

def reboot():
	cmd = "shutdown -r"
	p = subprocess.Popen(cmd, shell=True)
	p.wait()

def check_file():
	error = ''
	with open(file_path, 'r') as f:
		text = f.read()
		try:
			error = re.findall(r'\n\S+\s+RUNIC ERROR Problem 93, Error 702.37[^\n]*', text)[0]

			with open("error.log", "a") as e:
				e.write(error)
				e.write("\n\n")
				e.close()

		except:
			f.close()
			return False
		f.close()
		
	text = re.sub(r'\n\S+\s+RUNIC ERROR Problem 93, Error 702.37[^\n]*', '', text)

	with open(file_path, 'w') as f:
		f.write(text)
		f.close()
	return True



while True:
	if __name__ == '__main__':
		if check_file():
			reboot()
		# time.sleep(60)
		exit()



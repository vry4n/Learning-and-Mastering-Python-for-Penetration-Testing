- [ ] Create an FTP Object
	- [ ] ftplib.FTP(ip)
	- [ ] ftp.login(user, pass)
	- [ ] quit()
- [ ] Capture the Failed exception
	- [ ] Try, Except
- [ ] Read a user & password file
	- [ ] Iterates through user's file
	- [ ] For each username, reset the password file's read pointer to the beginning
	- [ ] Call the main_ftp function
- [ ] Create Main function to run the scripts
	- [ ] Check if the correct number of command-line arguments
		- [ ] If not, exit
		- [ ] Set IP, user & password variables

# Description
FTP brute-forcing is a technique used to gain unauthorized access to FTP servers by systematically trying various username and password combinations. While FTP has largely been superseded by more secure protocols, it's still prevalent in some environments, making it a potential target for attackers.

# Libraries
ftplib
sys

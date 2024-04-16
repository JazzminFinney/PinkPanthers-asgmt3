ftp_server.py

Description:
------------
This file acts as a simple File Transfer Protocol server, letting clients connect to it, check out the files in its directory, upload new files, download existing ones, and close the connection whenever needed.

Compilation:
------------
1. Open a terminal or command prompt.
2. Navigate to the directory containing 'ftp_server.py'
3. Use command 'python ftp_server.py'

Running the File:
-----------------
After executing the file using the above command, the server starts running on port 12000. Clients can connect to this port and start using commands like LIST, RETRIEVE, STORE, and QUIT to interact with the FTP server.

// // //

ftp_client.py

Description:
------------
This file acts as a simple File Transfer Protocol client. It lets users connect to an FTP server, find and list the files it has, add new ones, download existing ones, and drop the connection when they're done.

Compilation:
------------
1. Open a terminal or command prompt.
2. Navigate to the directory containing 'ftp_client.py'
3. Use command 'python ftp_client.py'

Running the File:
-----------------
After executing the file using the above command, the client will guide you through entering commands. You're given the following options: CONNECT, LIST, STORE, RETRIEVE, and QUIT. Use CONNECT to connect to the FTP server, LIST to see what files it has, STORE to upload files, RETRIEVE to download them, and QUIT to sign off.
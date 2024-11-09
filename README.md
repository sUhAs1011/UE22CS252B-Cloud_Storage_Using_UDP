To refine your project description and instructions, here’s a more structured and detailed format:

---

# Cloud Storage using UDP

### Overview
This project, developed as a mini-project for the fourth-semester Computer Networks course, demonstrates a cloud storage system based on UDP, employing a client-server architecture with Python Socket Programming. The functionalities include file upload, download, listing files (`ls`), and command execution (`cmd`) on the server, based on client requests.

### Requirements
1. Install the required Python modules (e.g., `socket`, `ssl`, etc.) before running the code.
2. Ensure both client and server systems are on the same network.

### Network Configuration
- **Single System:** Use "localhost" as the IP address for both client and server.
- **Multiple Systems:**
   - The **client** should use the server's IP address.
   - The **server** should set the IP address to "0.0.0.0" to allow connections from external clients.

### SSL Certificate
The file `cert.pm` is the SSL certificate used to secure communication between the client and server.

### Running the Application

- **Server:**
   ```shell
   python server4.py
   # or
   python3 server4.py
   ```

- **Client:**
   ```shell
   python client4.py
   # or
   python3 client4.py
   ```




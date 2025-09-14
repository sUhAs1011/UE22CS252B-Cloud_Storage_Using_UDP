
# Cloud-Storage-Using-UDP: Fourth Semester CN Mini-Project

### Overview
This project, developed as a mini-project for the fourth-semester **Computer Networks** course, demonstrates a cloud file transfer system built on **User Datagram Protocol (UDP)** using a **client-server architecture** implemented with Python's Socket Programming. Unlike traditional cloud transfer systems that typically rely on **Transmission Control Protocol (TCP)** for its reliability and delivery guarantees, this system leverages UDP to prioritize speed and low latency.

UDP, being connectionless, lacks built-in error correction or delivery guarantees, making it less common for cloud storage applications. However, its minimal overhead and faster data transmission make it suitable for specific use cases where speed is critical, and some loss of reliability can be mitigated through custom mechanisms. This project showcases such an approach, enabling functionalities like:
- **File upload and download**: Allowing clients to transfer files to and from the server.
- **File listing (`ls`)**: Retrieving a list of stored files on the server.
- **Command execution (`cmd`)**: Enabling clients to execute commands on the server remotely.

By using UDP, the project demonstrates how a lightweight and efficient cloud storage system can be implemented while addressing the challenges of reliability and error handling through application-level logic. This innovative approach highlights the practical applications of UDP in scenarios where low latency and simplicity are prioritized, making it an excellent educational tool for understanding both the advantages and limitations of UDP in networked systems.


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

### Teammates

- Suhas Venkata(PES2UG22CS590)
- Sumukh GS(PES2UG22CS596)


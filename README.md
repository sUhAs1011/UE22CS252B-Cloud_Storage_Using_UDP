# Cloud_Storage-using-UDP

It is my fourth sem computer networks mini-project. As the part of course curriculum, we had to create python programs for client server architecture using Socket Programming

In this cloud storage project, we can upload and download files. Please install the essential modules before running the python code.

When the client-server files are ran on the same system, the ip-address should be "localhost", and when we are using multiple systems say 2, the client system should use server address and 
the server should use 0.0.0.0 as the ip address,ensure that both the client and server are on the same network

The cert.pm file is the ssl certifcate

Command for running the client side

```shell
python client4.py
      or
python3 client4.py
```

Command for running the server side

```shell
python server4.py
      or
python3 server4.py
```

My project has upload,download,ls and cmd options, based the request that the client sends,the server responds accordingly



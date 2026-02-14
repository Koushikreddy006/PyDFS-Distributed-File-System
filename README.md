# PyDFS – Fault-Tolerant Distributed File System

##  Overview

**PyDFS (Python Distributed File System)** is a distributed storage system inspired by the architecture of Google File System (GFS).
This project simulates how large-scale cloud systems manage file storage using a client–master–chunk server architecture.

It demonstrates:

- Distributed system design
- Client–Server communication using TCP sockets
- File transfer across storage nodes
- Modular backend architecture in Python

The system runs through a Command Line Interface (CLI) and showcases core distributed storage concepts.
---

## 🔗 Live Demo

 Try the interactive web application here:  
https://pydfs-distributed-file-system-tg73kznlmr5nvhtwyc26by.streamlit.app/#py-dfs-distributed-file-system-web-demo

This web demo allows users to upload files and simulate distributed storage functionality through an interactive interface built using Streamlit.


##  Architecture

The system consists of three main components:

 **Client** – Sends upload/download requests  
 **Master Server** – Manages metadata and system coordination (basic structure implemented)  
 **Chunk Server(s)** – Store actual file data  

Current implementation supports socket-based file transfer between client and chunk server.

## Key Features

###  Implemented

- Socket-based file upload  
- Client–Server communication (TCP)  
- Distributed node structure  
- Modular project design  
- CLI-based interaction  
- Local distributed storage simulation  

### In Progress

- File chunking (splitting large files into blocks)  
- Metadata tracking via master server  
- Data replication for fault tolerance  
- Failure detection using heartbeat mechanism  
- Multithreaded parallel uploads  
- Download and chunk merge functionality  

##  Workflow

1. Client sends upload request  
2. File is transmitted via TCP socket  
3. Chunk server receives and stores file in `storage/` directory  
4. Future enhancement: master-managed chunk allocation and replication  

##  Technologies Used

- Python  
- Socket Programming (TCP)  
- File Handling  
- JSON (for metadata storage)  
- Modular Backend Architecture  

##  Project Structure

PyDFS/
├── client/
│ └── client.py
├── master/
│ └── master.py
├── chunk_server/
│ └── chunk_server.py
├── utils/
│ ├── metadata.py
│ ├── logger.py
│ └── checksum.py
├── storage/
├── metadata.json
├── main.py
└── README.md


## Usage

# 1️ Start Master Server
python master/master.py

# 2️ Start Chunk Server
python chunk_server/chunk_server.py

# 3️ Start Client
python main.py

# Client Commands
upload file.txt
download file.txt
exit

## Getting Started
# Clone the Repository
git clone https://github.com/koushikreddy006/PyDFS-Distributed-File-System.git
cd PyDFS-Distributed-File-System











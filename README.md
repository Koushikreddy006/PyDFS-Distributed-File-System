📂PyDFS – Fault-Tolerant Distributed File System
## OVERVIEW
The **PyDFS (Python Distributed File System)** is a fault-tolerant distributed storage system inspired by the design principles of Google's Google File System (GFS).
It simulates how large-scale cloud systems store files by:
Splitting files into chunks
Distributing chunks across multiple storage nodes
Replicating data for fault tolerance
Managing metadata centrally
The system is built using Python sockets, multithreading, and modular architecture, demonstrating real-world distributed systems concepts.


## Key Features
File chunking (large files → smaller blocks)
Distributed storage nodes (chunk servers)
Replication (multiple copies for safety)
Metadata management (master server)
Heartbeat-based failure detection
Multithreaded parallel uploads
Logging & monitoring
Command Line Interface (CLI)


## Workflow
Client uploads file
File split into chunks
Master assigns servers
Chunks replicated across nodes
Client downloads & merges chunks


## Technologies Used
Python
Socket Programming (TCP)
Multithreading
File Handling
JSON Metadata
Logging

## Project Structure
PyDFS/
├── client/
│   └── client.py
├── master/
│   └── master.py
├── chunk_server/
│   └── chunk_server.py
├── utils/
│   ├── metadata.py
│   ├── logger.py
│   ├── checksum.py
├── storage/
├── metadata.json
├── system.log
├── main.py
└── README.md


PyDFS/
├── client/
├── master/
├── chunk_server/
├── utils/
├── storage/
├── metadata.json
├── system.log
└── main.py


## Usage
Start the System
Open 3 terminals:
Terminal 1 – Start Master Server
python master/master.py
Terminal 2 – Start Chunk Server(s)
python chunk_server/chunk_server.py
(You can start multiple servers for replication)
Terminal 3 – Start Client
python main.py
Client Commands
upload file.txt
download file.txt
exit


## Getting Started
1. Clone Your Repository 
git clone https://github.com/koushikreddy006/PyDFS-Distributed-File-System.git
cd PyDFS-Distributed-File-System
2. Install Requirements (optional)
If needed:
pip install -r requirements.txt
(Mostly only Python standard libraries are used)
3. Run the System
Starturce Master → Chunk Servers → Client











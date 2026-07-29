# Sokkel

A simple client-server project written in Python that demonstrates TCP socket communication using the standard `socket` library.

## Overview

The project consists of two programs:

* **sockel.py** – TCP server
* **client.py** – TCP client

The client connects to the server, sends a user-entered name, and receives a response.

If the client sends the word `world`, the server replies with `Exit` and shuts down.

---

# Project Structure

```text
Sokkel/
├── client.py      # TCP client
├── socket.py      # TCP server
└── README.md
```

---

# Requirements

* Python 3.8 or later
* The client and server must be connected to the same network or be able to reach each other using the configured IP address.

---

# Getting Started

## 1. Start the server

```bash
python socket.py
```

The server will start listening for incoming connections.

## 2. Start the client

```bash
python client.py
```

The client will ask for your name:

```text
Enter your name:
```

Example:

```text
Ivan
```

Server response:

```text
Received data: Hello, Ivan
```

---

# Stopping the Server

To stop the server, enter:

```text
world
```

The server will respond with:

```text
Exit
```

and then terminate.

---

# Configuration

The project uses the following default server address:

```python
('192.168.1.100', 8888)
```

If you are running the server on another computer or network, update the IP address in both files:

* `client.py`
* `socket.py`

---

# How It Works

1. The server starts and waits for a client connection.
2. The client connects to the server.
3. The user enters a name.
4. The client sends the name to the server.
5. The server processes the received data:

   * replies with `Hello, <name>`;
   * replies with `Exit` and stops if the message is `world`.
6. The client displays the server's response.

---

# Technologies Used

* Python 3
* TCP/IP
* Socket Programming
* UTF-8 Encoding

---

# Example Output

### Client

```text
Enter your name: Ivan
Received data: Hello, Ivan
```

### Exit Example

```text
Enter your name: world
Received data: Exit
```

---

# Author

Pavel Kodochigov

GitHub: https://github.com/kiirlink

---

# License

This project is intended for educational purposes. Feel free to use, modify, and learn from the source code.

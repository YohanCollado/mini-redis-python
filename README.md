# Mini Redis Python

A lightweight Redis-inspired in-memory key-value store built from scratch in Python to learn networking, systems programming, and database fundamentals.

## Overview

This project implements a simple TCP server that accepts Redis-style commands and stores data in memory using a Python dictionary. The goal is to understand how databases and caches work under the hood by building the core functionality from scratch.

## Features

* TCP client-server architecture
* In-memory key-value storage
* Command parsing and execution
* Redis-style commands:

  * `SET key value`
  * `GET key`
  * `DEL key`
  * `PING`
* Multiple client connections (one at a time)
* Simple request-response protocol

## Example Usage

Start the server:

```bash
python server.py
```

Connect with a client:

```bash
nc 127.0.0.1 6379
```

Example session:

```text
PING
PONG

SET name yohan
OK

GET name
yohan

DEL name
DELETED

GET name
NULL
```

## Architecture

```text
Client
   │
   ▼
TCP Socket
   │
   ▼
Mini Redis Server
   │
   ▼
In-Memory Dictionary
```

### Request Flow

```text
Client sends command
        │
        ▼
Server receives bytes
        │
        ▼
Command is parsed
        │
        ▼
Store is read or modified
        │
        ▼
Response returned to client
```

## Technologies

* Python 3
* Socket Programming
* TCP Networking

## Concepts Learned

This project explores several fundamental systems concepts:

* TCP/IP networking
* Client-server architecture
* Command parsing
* In-memory databases
* Request-response protocols
* Key-value storage systems
* Data persistence foundations

## Future Improvements

* Custom Python client
* Key expiration (TTL)
* Persistent storage
* Append-only log (AOF)
* Concurrent clients using threads
* Publish/Subscribe messaging
* Replication
* Distributed clustering
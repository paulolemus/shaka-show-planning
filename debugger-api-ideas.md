# Debugger API Ideas

## Information we might need from shaka-scheme

* Everything goes straight to c++ stdout and stderr

## Questions about Shaka-Scheme

is there gonna be any 
Set of prodecures that interat with VM.
Big picture goal is complete integration.

Sub goal - Get wire working, we can send c++ a query and send back a response.

All classes called all the time, they have internal state which can be managed through Wire.
They can be set to be active or not, they can be rearranged by wire, 
DBAPI folder tht has all classes to use.

Maintain active set and inactive set where a class instance from one of the procedures live.
Only active ones get moved to active set.
They will be singleton classes.

What if we want to pause.


This is very OOP.

Functional approach:
Model each procedure as pure functions with callbacks.



## Required Shaka-Scheme features

* Need to make implementation of VM
* VM checks before and after each instruction for requests.
* Poll for messages using zmq in async fashion.
* Tell shaka-scheme what ports to use.
* Convert Data objects to JSON?
* capture STDOUT and STDERR
* Asyncly pipe stdout/err to zmqsocket.
* Uniquely identify environments
* Pass all messages through schema filter

## Messaging schema notes

* All data is sent over ZMQ sockets.
* Python has support for json, such as parsing python objects from json string or turning python objects into json string.
* C++ has one decent json library, it is a little verbose.
* Python easily supports JSON schema validation, C++ not so much.
* Consider binary serialization when sending json vs as string
* Need a way to represent shaka::Data as json
* Each message should contain a timestamp it was sent.
* pyzmq has support for parsing JSON sent over wire.
* Command packets, response packets, and data packets.

What we care about receiving:
For variable watch:
* command packet to request watch on specific symbol in environment.
* Response saying request will be fufilled.
* Data packet containing variable name, value, environment.

For Env watch:
* Automatic?
* Data packet containing environment color, level, and key/value pairs in environment. name of parent environment?

Console:
* Type of message, stdout or stderr.
* Timestamp
* contents

## Specifc instructions

### Meta
Ping - get a return packet of ping type
kill - shutdown everything
port - Set port for publishers



modprocedure - Set state of procedures
getprocedures - Get all the procedures in their approriate order
getprocedure - get info on specific procedure.


### Prodecures

halt - halt until new instruction changes
step - move forward one instruction

Envwatch - 
    Levels to care about

Varwatch -
    push - list string
    pop  - list of string
    levels - 




## Messaging schema


## 

DB api - convert shaka-data or json to content sendable content. Worry about sending data.
inherit from heapvirtual machine


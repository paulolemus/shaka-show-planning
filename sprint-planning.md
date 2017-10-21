# Sprint Planning

## Tasks (in no particular order)

* Setup primary shaka-show repository, similar to JupyterNotebook (1)
* Setup project with Pycharm, make sure all modules work and can run
   a bare main testing script with each nesassary module imported (1)
* Make list of requests that are going to be made to Debugger API (2)
* Develop protocol (or format) in which messages will be sent between python client and shaka-scheme over zmq (3)
* How to enforce protocol standard in python and c++ implementations (?)
* Setup basic template and static structure (2)
* Write standard on how to use template sytem for panels, cs, and js (5)
* Compile base template with panel templates (1)
* Parse source file, send and display bare bones in source-code panel, no consideration for other imported source code (3)
* Serve compiled template index.html for viewing (2)
* Setup ZMQ mocking and testing to model request to interpreter and response (3)
* Develop start, pause, stop, step control requests in python over zmq (3)
* mock start, pause, stop, step control request and shaka-scheme responses (2)
* Setup communication sockets: 1=control request, 2=stdout/stderr sub, 3=request sub in python (?)
* Develop javascript for play button = ajax request to python client (2)
* develop js for pause btn (1)
* develop js for stop btn (1)
* develop js for step btn (0)

# Shaka-Show

Shaka-Show is a web-based visual debugger for the Scheme interpreter Shaka-Scheme.
The debugger will be used similarly to how gdb or jdb are used; it will be launched from the command line.
Say we have a Scheme program saved in hello-world.scm. It should be launched as follows:
```
shaka-show hello-world.scm
```
Shaka-Show will do several things here:
1. It will launch an instance of Shaka-Scheme with launch parameters to enable the Shaka-Scheme Debugger API.
2. It will start a python built webserver that handles communication between the web browser and the Shaka-Scheme interpreter. 
3. It opens a web browser to http://localhost:8888/ so we can begin to debug our program.


# Shaka-Show Purpose

The purpose of Shaka-Show is to create web based application in which the user can debug a scheme program running on the Shaka-Scheme interpreter.
We are making it web based so it can be very user / beginner friendly. Everyone is familiar with interacting with web-based applications, and with a set of simple controls or features, using the debugger should be a no-brainer.
The reason that we are making the debugger as a web-based application is so in the future we will be able to include a visual representation of the evaluation of source code.


# Shaka-Show Initial Features

Here are some of the features we are going to build:

1. A source code line tracker

   This is a panel located on the left side of the debugger app that displays the user's source code, as well as what line number is currently being evaluated. In other words, this shows the current line of execution.

2. Warning and Error Information

   This is a panel located on the bottom left of the debugger app. It is basically a console that displays any warning or error information that the interpreter generates. This includes stack-traces on catastrophic errors.

3. Environment Watch

   This is a panel that displays to the user the variables in the current environment.

4. Variable Watch

   This is a panel that displays to the user particular variables through out the life of the program and information such as the value and located environments.

5. API Controls

  API Controls refers so far to the following user controlled capabilities:
  * Start
  * Pause
  * Resume
  * Stop
  * Restart
  * Step forward


# Paulo only - Develop architecture TODO

Here are some of the things I need to do to select and understand the technologies we are going to use.

1. Go through basic Python tutorials - DONE
2. Create a sample Tornado(?) that serves html and javascript over HTTP. - DONE
3. Create a C++ server and Python client that communicate via ZeroMQ sockets by JSON.
4. Look into Tornado for Python
5. Draw architecture on paper
6. Finalize technologies
7. Make Python "tutorial" session to get everyone introduced to modules, TDD, IDE, JSON
8. Plan assignments for the following sprints

# Python Notes

* No semicolons
* datatypes: boolean, int, float, complex, str, bytes, list, tuple, set, dict, list
* string made with " and ' are exactly the same.
* interal string to script should be made with ', any string user will see should have "
* No braces. Indentation is used for blocks. 4 spaces mean one block up.
* Use camelCase.
* Booleans are denoted with capital True or False.
* Comments start with "#"
* Multi-line comments are enclosed in """ (triple quotation marks)
* exponents are done with \*\*
* input() returns string. Need to cast to something else to use as int or float
* % operator is used after a string to combine a string with variables

Control flow
* and, or, not are all boolean operators
* order of operations: not, and, or
* control statements: if, for, while 
* Use 'pass' keyword for empty blocks of code.

Functions
* Functions are objects.
* declare function with the def keyword
* Parameters are passed by reference(?)

Classes
* define with keyword class
* private variables are made with two underscores by convention



# Python Modules

* webbrowser
   Used for opening a webbrowser and navigating to a specific address
   https://pymotw.com/2/webbrowser/

* tornado
   A Python web framework and asynchronous networking library.
   Is ideal for long polling, websockets applications.
   Stands inbetween Django and Flask
   http://www.tornadoweb.org/en/stable/

* jinja2
   the most popular Python template engine.
   http://jinja.pocoo.org/docs/2.9/

* json
   A JSON parsing library. Super simple, turns json string into dict.
   https://docs.python.org/3/library/json.html

* argparse
   A module that makes it super easy to parse through commandline arguments.
   This will be used to define optionns when launching shaka-show \<program-name\>
   https://docs.python.org/3/library/argparse.html

* subprocess
   A module used to execute programs as subprocesses of the current.
   Can be used potentially to communicate with shaka-scheme

# Resources

https://github.com/jupyter/notebook
 - Going to use this resource as a model for architectures, source structure.


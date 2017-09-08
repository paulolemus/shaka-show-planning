# Shaka-Show Architecture

## Shaka-Show file structure

* shaka-show
    * docs/
    * shaka-show/
        * static/
        * templates/
        * 
    * .gitignore
    * README.md
    * \<various other project wide configurations\>

## What Shaka-Show needs from Shaka-Scheme

* We need to be able to modify Vm registers via debugger API.
Possible methods:
Have the non-blocking zmq receiving socket code running in a async task or a thread. When any API requests are made by the debugger client, they will be added to a queue that is accessable by the VM. The debugger API in shaka-scheme will then set a flag indicating changes have been made, which the VM checks before each instruction. Alternatively, could have the VM check the queue directly before each instruction.
To change the instruction once the VM is aware of the request, could pass references of each register into a function that does the corresponding request made by the debugger API, such as HALTing, or resuming from a halted state.

* We need to be able to step through instructions
Possible method:
In the debugger enabled VM, could have a couple modes of operation.
The mode would be initially set to a default, or a commandline argument.
One mode would be step, so it would execute one instruction, then swap the current instruction with a halt, and then listen for debugger API communication.

* Need to receive warning and error information
Method:
This might be really easy. If we are already sending these warning/error messages to stderr, we could do either one of the following:
Send string on stderr/stdout broadcast channel (made with zmq). It should be as easy as setting up a subscriber for the channel in the debugger client, which would then relay the text to the Warning and Error fake console of the web app.
Directly capture stdout/stderr via "subprocess" module when launching shaka-scheme from shaka-show.

* Environment watch
Method:
Debugger client is subscribed to shaka-scheme publisher that will publish anytime there is a change to the environment. Should be sent as a JSON dict when a key's value is changed on shaka-scheme. This will mostly be written into the debugger VM.

* Variable watch
Method1:
Client sends request and variable to debugger API, debugger keeps a map of variables being watched, as well as most recent state. Each instruction, could compare current state to previous state and if it changed, publish on zmq socket.
Method2:
Have VM publish each variable every instruction.

* Source code line tracker
Should be able to display original source code with no problem, have not yet gotten to syntax-object implementation ideas.

# Shaka-Show client logic

Shaka-Show
1. launch shaka-show with name of program to debug
2. execute primary Tornado "Application" class to first ensure that zmq handlers are subscribed to appropriate addresses.
3. Launch shaka-scheme as a sub-process with args that provide the source file name and that enables the debugger API.
4. Shaka-Show client now serves primary web app, opens default browser to localhost:8888/, and sends keep-alive/ping request to debugger API, which should respond.
5. When the user wishes for something to happen, user will interact with web app. Javascript will send the corresponding requests to the Python Server, which will then interpret them (each request should have its own handler) and send the corresponding request to the Debugger API. When the debugger API has received or completed the request, it sends a corresponding response.


# Timelines:

9/11 - Have client project folder setup, delegate tasks
9/18 - Have main .html template working with two unfinished panels
9/18 - Finish basic Source code tracking panel
9/24 - Get AJAX js requests working for API control buttons
9/24 - Finish commuication protocol
9/24 - Mock messages from shaka-scheme
10/1 - Have partially working syntax object class with parsing
10/8 - If VM is nearly finished, begin working on C++ ZMQ debugger API

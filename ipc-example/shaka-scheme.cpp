

#include <zmq.hpp>
#include <string>
#include <iostream>
#include <unistd.h>

int main() {
    zmq::context_t context(1);
    zmq::socket_t socket(context, ZMQ_REP);
    socket.bind("tcp://*:8989");

    while(true) {
        zmq::message_t request;

        socket.recv(&request);
        std::cout << "Received request: " << std::endl;

        sleep(4);

        zmq::message_t reply(5);
        memcpy(reply.data(), "Suppp", 5);
        socket.send(reply);
    }
    return 0;
}

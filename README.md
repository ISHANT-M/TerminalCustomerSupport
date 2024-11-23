# Terminal based Customer Support
#### REQUIRMENTS
- python (preferably version 3)
- sockets module

#### FEATURES
- easy to use
- gives support exec moderation controls
- customer can only send messages when support exec wants to take any input

##### FOLDERS
###### tests
it is an echo terminal chat where client send message to server which is then sent back to the client's computer.
- contains sample code to test the correct installation of python3 and sockets module.
- first run server file which will wait for incomming connections.
- next run client file which will connect to the server.

###### src
it contains main source code related to our project.  
- first run server code on the support exec's machine, and then run client code on customer's machine.
- only the server has permission to send messages, for server to take response from the client, exec has to allow customer to send something in the chat by sending %rcv% in the chat.



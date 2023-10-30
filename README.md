# simulinkTCP_Send
While trying to figure out how to export data from a Simulink model in real time, I found many questions, but not many answers.
I'll create this documentation to help those still searching for the answers.

A sample code on receiving data points from a Simulink model.

Required add-on:

<img width="600" alt="Screenshot 2023-10-30 at 12 32 32" src="https://github.com/izlim/simulinkTCP_Send/assets/53293158/a05a3078-6141-46ff-8555-d46e9274beb4">

The model is a simple one that outputs data in double format.

<img width="350" alt="Screenshot 2023-10-30 at 13 16 15" src="https://github.com/izlim/simulinkTCP_Send/assets/53293158/3e0ccca8-24ce-401c-b890-63139d801f60">

The TCP/IP Client Send block has to be configured as follows.

<img width="350" alt="Screenshot 2023-10-30 at 13 05 09" src="https://github.com/izlim/simulinkTCP_Send/assets/53293158/0ffd8db9-4945-4484-afa1-293bce9bd03a">

It's important that the byte order is set to little-endian, if not, the data will be sent in the wrong order.

The Python Server will receive the data as 8 bytes and unpack it into a double.

# Overview

I used VScode to create two python programs for this project. This project requires codes because one belongs to the server and one to the client. For the client to be able to input their input they have a simple GUI that was made. However, without the server code running there will be no connection between the client to the API server that has the information they are requesting. This is where the server code comes in. In the server code, it will allow the client to connect to the API regarless of location because it establishes a connection via a API key that was given from the API. This key is like the password that allows the user access to the API's information when requested. If the Server code does not have one or has a incorrect key it will not allow the client to pass and retrieve the information they are requestiong. 

The purpose of this project was to show skill aquired regarding using the network to connect two devices with each other. It shows that I understand the concepts of how to ping, request, and retrieve information between devices. I choose weathe because it is something that people check on every single day around the world. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

I choose to do a client/server architecture. This is done by having two different codes work together to ping and request and retrieve the desired information. The client code is the most important as it works as the middle man between the client and API host. Without it there is no communication between them at all.

I used TCP and the port numbers used were: 65432

On the Server Side of things as the server program is ran it will display in the terminal any message you want that it is up and running. This allows us to know that they server is just waiting now for input from the client. For the Client they have a GUI with a output area that will communicate with them regarding the requests. For requesting, there is a input box with a button to submit the request. 

# Development Environment

{Describe the tools that you used to develop the software}
I used Python as the language of this project. This was done with the program VScode. Along with using a API online and their API key. 

{Describe the programming language that you used and any libraries.}

I installed Python to use as my Language.

{Make a list of websites that you found helpful in this project}
* [Linkedin]https://www.linkedin.com/advice/3/how-can-you-compare-peer-to-peer-networks#:~:text=Client%2Dserver%20networks%20are%20more,cost%2C%20complexity%2C%20and%20maintenance.
* [Geeksforgeeks](https://www.geeksforgeeks.org/client-server-model/)
* [educative.io](https://www.educative.io/answers/how-to-implement-tcp-sockets-in-c)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Make the results end up in the GUI for client not the Server Terminal
* Create a visual result instead of Characters
* Better and More Advanced GUI
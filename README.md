# AutoLock

The purpose is to have a lock that can be opened or closed by a user from a mobile device. Raspberry pi 3 was used for this project. This access would be password protected, but would also use an implementation of an AES-RSA hybrid encryption algorithm.

The raspberry pi would run the server.py on boot using Flask, and would listen for incoming HTTP messages. 

The idea is that when a particular password is sent to the raspberry pi server (like post.py does), it should run the test1.py, which would turn the motor connected to the raspberry pi to open the lock.

The password would be encrypted and decrypted as shown in the Cryptosystem.txt file. 

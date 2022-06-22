# Secure-File-Sharing-Using-Cloud
A system to Securely share file with multiple users on the cloud 

## Introduction 

In the current era, Cloud has become an irreplaceable part one’s life. From storing a large sized
backup data to instantly sharing a file to each other, cloud is being used in our daily lives
frequently. Invention of cloud computing has solved numerous problems which were hard to deal
with. With all the bright side of cloud computing, there are some problems which need to be
addressed as well. One of those problems is security issues. A file being shared on a wireless
medium is vulnerable to many threats and put risks on its privacy. This project is a try to solve
this problem using encryption and key exchange algorithms. This method can also be useful when
the users are putting their data in a third-party cloud storage. It will reduce the risk of data theft
and data misuse by any person with mal-intent. This threat keeps on increasing as we increase
the size of organization. Many large companies and government bodies are researching ways to
deal with this kind of dangers and provide more secure transaction of files through cloud. These
researches have provided us with some powerful encryption and key exchange algorithms. Some
of the algorithms are said to be uncrackable even using current super computers. AES encryption
and Diffie Hellman Key Exchange are one of those algorithms which we will use in our project. 

## System Design

This system is designed such that it can be differentiated in two parts. The main aim for doing
that is easier maintenance on later part and work division between group members. The first
part is consisting of a computer application. The task of this application is to become a bridge
between the web-hosting application and user’s computer device. This application will be used
to encrypt and decrypt any given file using various keys. The application will be using a symmetric
key encryption-decryption technique. The second part will be a web application. This webapplication will act as a user portal. The web-application will register any new user. It will also
allow users to download any already registered user’s public key. Also, the web-application is
hosted on a cloud service which enables it to store a file from a registered user. A registered user
can also download encrypted file uploaded from any user.
For better understanding of flow of the process, let us consider a simple case. Let suppose a
person X is trying to send a file to person Y using our service and both parties have already
registered on web-application. Now, person X can download the public key of person Y. Person
X will use our computer application to encrypt the file he wants to send, using his private key and
person Y’s public key. Then person X will upload the encrypted file on the cloud using our web
application. Now person Y can see the file in file list of web application and download it. Once
person Y has downloaded the file, he will use the computer application and decrypt the file using
his own private key and person X’s public key. After the decryption, person Y can see the original
content sent by person X. Now, for an instance, person Z is trying to pry in the file sent by person
X. Even though person Z has access to public key of person X, he will not be able to decrypt the
file without private key of person Y. 

## Algorithms Used 
### Diffie Hellman Key Exchange
  Diffie Hellman key exchange (DH) is also referred as exponential key exchange. This name is
related to the fundamentals of this method. It is a cryptographic method which uses different
predefined numbers raised to certain powers as keys. This predefined numbers are never
transmitted, rather discussed before the transmission begins. Now we will see how the
algorithm is used.
Consider the above scenario, Alice and Bob wants to communicate using cloud. They have
decided the value of P and G. First, they start by generating the private key for themselves.
Then they will generate a public key using P, G and their private key. As we can see, for each
time of encryption and decryption one private key is need. At the time of encryption, sender’s
private key will be used and at the time of decryption receiver’s private key will be used.
Though values of P, G and public of both parties is known publicly, there is no way to obtain
the secret message (3) by using these number. There are certain limitations to it as well. Like
the decided value of P and G will decide how many users can exist simultaneously in the
environment. As they can not be change later on and increasing their value will also increase
the computational power required, a careful planning is needed. The second limitation is the
private-key generator. One can say that it is the most vulnerable part of the whole algorithm.
If someone have access to it, they can know the method of generating the private key. 

### Advanced Encryption Standard (AES)
Advanced Encryption Standard (AES) is one of the most widely used encryption methods. It
was established by U.S. National Institute of Standards and Technology (NIST). AES is said to
be stronger and more secure than the DES or triple DES. This can be achieved by larger key
size which prevent the exhaustive key search attack.
The AES consist of three fixed 128-bit ciphers with key size 128, 192 and 256 bits with 10, 12
and 14 rounds of encryption. These arounds are depended on key length required. Key size
can be very large but the block size maximum value can be up to 256 bits. The AES design is
based on SPN networks which is also known as substitution-permutation network. 

## Implementation

The project is made of two parts. The computer application and the
web application. To understand the implementation of these parts, let suppose a sender wants
to send a file to a receiver. First, sender will visit our web application, where they can see the list
of all the available users. From there, sender can download the public key of receiver. Then,
sender will use the computer application to encrypt the file using their own private key and
receiver’s public key. This computer application is build using python modules like tkinter, crypto
and secret sharing algorithm. The file will be encrypted using AES. The encrypted file will be then
presented to the sender. Now, sender will use the web application to upload the encrypted file
on to the cloud.
The web application is constructed using python flask, HTML, CSS and bootstrap. This web
application is hosted on a cloud service provider. Receivers can see the list of all user and
download the public key of the sender of the file. Then after, receiver can download the
encrypted file. Now to decrypt the file, receiver must provide the computer application with their
private key and the sender of the file’s public key. Then only then, the file will be decrypted
successfully and contents can be seen by the receiver. The Web application also have ability to
register a new user and provide them with unique private key. Then web application will show
the public key of the newly added user in the list of users. 
### Example 
#### 1) This is our original file that sender wants to submit.
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/1.png"></img>
#### 2) This is where we will encrypt our file with 2 keys.
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/2.png"></img>
#### 3) This is the content of encrypted file. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/3.png"></img>
#### 4) This is the home screen of our web application. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/4.png"></img>
#### 5) This is Where user can upload the encrypted file. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/5.png"></img>
#### 6) The screen after the uploading a file is done.
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/6.png"></img>
#### 7) List of all the encrypted files which can be downloaded. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/7.png"></img>
#### 8) List of public keys of registered users. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/8.png"></img>
#### 9) Then the download file can be decrypted using the receiver’s private key and sender’s public key. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/9.png"></img>
#### 10) This is where a user can register. 
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/10.png"></img>
#### 11)  Final screen after registration of new user.  
  <img src="https://github.com/meetc-8581/Secure-File-Sharing-Using-Cloud-/blob/main/Images/11.png"></img>

## Summary 

This system is capable of sending files from a single user to another single user securely using
cloud. As AES is highly secure, decrypting a file without proper keys can take more than a million
years with highest level of computation power. Though, this environment also presents us with
some other challenges as well. This system is not optimal if a user wants to share a file to multiple
users. In that case, sender must encrypt the file using all the receivers’ public key which will create
many redundant data and computational overhead for sender. 

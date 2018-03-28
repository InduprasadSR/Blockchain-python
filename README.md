# Blockchain-python

Block Chain: The blockchain is an undeniably ingenious invention.
A general ledger concept is making baby steps in global IT market.
Moving your IT infrastucture to a block chain makes tremoundous changes in your Business module.

Where you can impliment a general ledger?
Well thats pretty interesting, you can use anywhere which includes centralised system's containing huge data like transaction data in Financial 
services, patient medical records in Health care and so on.
These datas will be available to every nodes which connected to a block chain network.

Since block chain gives you decentralised or peer to peer arcitecture , you no need to worry about data lose.

Python : Python is one of the best way to form and impliment your block chain system. 
Here i used python2.7 and flask for API and front end.

Installation:

1. Install Python 2.7 or above 
2. Install Python flask "pip install flask"
3. Install requests library "pip install request"


This repository contains 2 services 

1. Services library : which holds all ledger configuration. All data will be insrted within this port.
 "LedgerService.py" contains coding for services.
	*****"Execute this file first"****
  Once you run this library it will be serving in  PORT:5000.
  All GET and POST will happen through this lib.

2. WebView: contains flask related libraries and its HTML format to view data or add any transactions.
  "flask_index.py" is taking care of this part.
	*****"Execute this file after execution LedgerService.py"**** 
   once you run this file it will be serving in "your-system-ip/localhost":5004

To open in browser  "your-ip":5004/login  or localhost:5004/login
Which will open login screen.

Provide "admin" as username and "password" as password.
Username and Password been hard coded as of now, later can be added with local .db connection.


Once you login you will be navigated to /index where you can add sample transaction and you can view the same in same page.

So far i have created a form which only makes a sample transaction and generates its 256 hash code.
Based on your requrement change the form and API structure and its valiation.


How to connect a new node to make a peer to peer network?
	To connect a new system you should give any system ip which is alredy connected in the network.
For very first connection give your own system ip.










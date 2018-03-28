from flask import Flask
from flask import jsonify
from flask import request
import hashlib
import time
import datetime
import requests


app = Flask(__name__)

generalLedger=[]

All_IPv4_lot=[]


@app.route('/getAllTransactions',methods=['GET'])
def getAllLedger():    
    unique = { each['hashcode'] : each for each in generalLedger }.values()
    return jsonify(unique)

@app.route('/getAllTransactions/<hashcode>',methods=['GET'])
def getLedgerwithHash(hashcode):
    Ledger = [ led for led in generalLedger if (led['hashcode'] == hashcode) ] 
    return jsonify({'SpecificLedger':Ledger})


@app.route('/AddThroughPortal',methods=['POST'])
def createTransactioninPortal():
    if not(request.form['From']=='' or request.form['To']==''):
        From=request.form['From']
        To=request.form['To']
        Amount=request.form['Amount']
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        hashCode= hashlib.sha256(From+To+Amount+st).hexdigest()
          
        
        Newdata = {
        'hashcode':hashCode,
        'From':From,
        'To':To,
        'Amount':Amount
        }
        generalLedger.append(Newdata)
        return 'Wow! your transaction is successful!'
    else:
        return 'Invalid transaction'


@app.route('/AddTransaction',methods=['POST'])
def createTransaction():
    if not(request.json['From']=='' or request.json['To']==''):
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        #hashcode= hashlib.sha256(request.json['From']+request.json['To']+request.json['Amount']+st).hexdigest()
                         
        Newdata = {
        'hashcode':request.json['hashcode'],
        'From':request.json['From'],
        'To':request.json['To'],
        'Amount':request.json['Amount']
        }
        generalLedger.append(Newdata)
        return jsonify(Newdata)
    else:
        return 'invalid transaction'

@app.route('/postip',methods=['POST'])
def addIp():
    NewIp = {
    'ipv4':request.json['ipv4'],
    }
    All_IPv4_lot.append(NewIp)
    return jsonify(NewIp)


@app.route('/getip')
def getAllIp():
       
    return jsonify(All_IPv4_lot)

   

if __name__ == '__main__':
   app.run(host= '0.0.0.0', port=5000)

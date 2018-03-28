from flask import Flask,render_template
import json
import urllib2
import requests
from json2html import *
from flask import Markup
from flask import jsonify
from flask import request
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
app = Flask(__name__)

ipv4_lot=[]


FirstPeerIp=raw_input("Enter ip of your friendly network!")



def post_json_request(ipv4_json):
    url='http://'+FirstPeerIp+':5000/postip'    
    req = urllib2.Request(url)    
    req.add_header('Content-Type','application/json')    
    headers = {'content-type': 'application/json'}
    #url='http://+'FirstPeerIp'+:5000/postip'    
    r = requests.post(url, data=ipv4_json,headers=headers )
    #print r.text

def  get_all_ip():
    urlget='http://'+FirstPeerIp+':5000/getip'
    reqget = urllib2.Request(urlget)
    reqget.add_header('Content-Type','application/json')
    headers = {'content-type': 'application/json'}
    getFromFriendlyNetwork = requests.get(urlget,headers=headers )
    #print getFromFriendlyNetwork.text
    data=getFromFriendlyNetwork.text
    ipv4_lot={}
    ipv4_lot=json.loads(data)
    for item in ipv4_lot:
        data = json.dumps(item)
        #print data
        url='http://127.0.0.1:5000/postip'
        req = urllib2.Request(url)  
        req.add_header('Content-Type','application/json')    
        headers = {'content-type': 'application/json'}
        url='http://127.0.0.1:5000/postip'    
        r = requests.post(url, data=data,headers=headers )
        


        
import socket 
connectedDevices=[ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1]


my_ip=socket.gethostbyname(socket.gethostname())
NewIp={
      "ipv4":connectedDevices
      }

NewIp=json.dumps(NewIp)
ipv4_lot.append(NewIp)

post_json_request(NewIp)   
get_all_ip()

NewIPget='http://127.0.0.1:5000/getip'
Newreqget = urllib2.Request(NewIPget)
Newreqget.add_header('Content-Type','application/json')
headers = {'content-type': 'application/json'}
New_Ip_Lot=requests.get(NewIPget,headers=headers )
New_Ip_Lot=json.loads(New_Ip_Lot.text)
#All_Unique=json.dumps(New_Ip_Lot)
#print All_Unique
#unique = { each['ipv4'] : each for each in All_Unique}.values()
#print jsonify(unique)
#print len(New_Ip_Lot)




               


@app.route('/index', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return render_template('index.html')
    else:
        flash ('wrong password!')
    


@app.route('/getAllTransaction')
def get_all_data():



   for i in range(0,len(New_Ip_Lot)): 
       ustr=' '.join(New_Ip_Lot[i]['ipv4'])
       url='http://'+ustr+':5000/getAllTransactions'
       headers = {'Accept': 'application/json'}
       r = requests.get(url,headers=headers )
       data_local=r.text
       load_Local={}
       load_Local=json.loads(data_local)       
       #load_Local=json.dumps(load_Local)       
       for item_local in load_Local:
           data = json.dumps(item_local)
           
           if (ustr!=my_ip):
               url_local='http://127.0.0.1:5000/AddTransaction'
               req_local = urllib2.Request(url_local)  
               req_local.add_header('Content-Type','application/json')    
               headers = {'content-type': 'application/json'}
               url_local='http://127.0.0.1:5000/AddTransaction'
               update_local = requests.post(url=url_local, data=data,headers=headers )
               
   url='http://127.0.0.1:5000/getAllTransactions'
   headers = {'Accept': 'application/json'}
   r = requests.get(url,headers=headers )
  
   HTMLbody="""<head><style>
           table    { 
           border-spacing: 1; 
           border-collapse: collapse; 
           background:white;
           border-radius:6px;
           overflow:hidden;
           max-width:800px; 
           width:100%;
           margin:0 auto;
           position:relative;
              }

               tr {
              background-color: #def;
               }
            th {
              background-color: #cba;
            }
            td {
           width: 30%;
           height: 30px;
           color: red;
           background: transparent;
            }
           
          </style>
        
          </head><body>"""

    #<meta http-equiv="Refresh" content="1">
   HTMLtable=json2html.convert(json = r.json(), table_attributes="id=\"info-table\"  border=\"1 px \"  background-color: \"#4CAF50\" width=\"100%\" class=\"table table-bordered table-hover\"")
   HTMLCom=HTMLbody+HTMLtable   
   return  (HTMLCom)
 
   

@app.route('/AddSystemIpview')
def ipsets():
    return  jsonify(ipv4_lot)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return render_template('login.html')
   

@app.route('/')
def index():
   if not session.get('logged_in'):
      return render_template('login.html')
   else:
      flash ('wrong password!')
           

if __name__ == '__main__':
   app.secret_key = os.urandom(12)
   app.run(host= '0.0.0.0', port=5004 )

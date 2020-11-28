# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 00:22:01 2020

"""

#*****************************************************************************************#
#```from original source file to hashed versions                                          #
#```only getting from_address and to_address:(from_address, to_address)                   #
#```contract_net_address_hash.csv: (address, hashID)                                      #
#```````hashID start from 0                                                               #
#```````address comprises all distinct addresses from 'from_address' and 'to_address'     #
#```contract_net.csv: (hashed_from_address, hashed_to_address)                            #
#```if more attributes is needed, feel free to add them in                                #
#```taken from `bigquery-public-data.ethereum_blockchain.traces`                          #
#```taken from `bigquery-public-data.ethereum_blockchain.contracts`                       #
#*****************************************************************************************#
'''
Some transactions create smart contracts from their input bytes, and this smart contract is stored at a particular 20-byte address.
This table contains a subset of Ethereum addresses that contain contract byte-code, as well as some basic analysis of that byte-code.
Introduction of contract net, this means trace/transaction create from2015 should have same address recorded as smart contract addr

statusEither 1 (success) or 0 (failure, due to any operation that can cause the call itself or any top-level call to revert)
'''
import csv
import sys
import datetime
maxInt = sys.maxsize

while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)
print("start: ", datetime.datetime.now())
#csv.field_size_limit(sys.maxsize)


a = 0
nodes = {}
contracts = {}
n = 0
count= 0
path1 ="E:/blockchain data at sch/New folder/blockchain/submission/original/trace/"
path2 ="E:/blockchain data at sch/New folder/blockchain/submission/original/contract/"

with open(path2+"contracts2015.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})
                
with open(path2+"contracts2016.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})

with open(path2+"contracts2017.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})
                
with open(path2+"contracts2018.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})   
    
with open(path2+"contract2019_consolidate.csv", "r") as cFile:
        reader = csv.reader(cFile)
        for rows in reader:
            if rows[0] != 'address':
                contracts.update({rows[0]: "sc"})   
                
#contract2019_consolidate
#while a < 5000 :
#    if a < 10:
#        f = 'traces'+filenum1+str(a)+'.csv'
#    elif a <100:
#        f = 'traces'+filenum2+str(a)+'.csv'
#    elif a < 1000:
#        f = 'traces'+filenum3+str(a)+'.csv'
#    else:
#        f = 'traces'+filenum4+str(a)+'.csv'
        
    #['transaction_hash', 'transaction_index', 'from_address', 'to_address', 'value', 'input', 'output', 'contract_type', 'call_type', 'reward_type', 'gas', 'gas_used', 'subcontracts', 'contract_address', 'error', 'status', 'block_timestamp', 'block_number', 'block_hash']
f = path1+"trace2019_consolidated.csv"
print("start: ", datetime.datetime.now())
with open(f, "r") as gFile:
    reader = csv.reader(line.replace('\0','') for line in gFile)
    with open(path2+ "contract_net2019_full.csv", "a+", newline ='') as tfile:
        writer = csv.writer(tfile)
        for rows in reader:
            try:
                if rows[2] != 'from_address':
                    # row[15]is status
                    if rows[15] == '1':
                        if ((rows[2] != '') and (rows[3] != '')):
                            # in the same time, this address can be found in contract net, means, it is smart contract 
                            if ((contracts.get(rows[2]) is not None) and ((contracts.get(rows[3])) is not None)):
                                #<e, from, to, value, gas, gas used, txnhash, contract addr, contract type, block num>
                                if nodes.get(rows[2]) is None:
                                    nodes.update({rows[2] : n})
                                    n+=1
                                if nodes.get(rows[3]) is None:
                                    nodes.update({rows[3]: n})
                                    n+=1
    
                                writer.writerow([nodes[rows[2]], nodes[rows[3]]])
                                count +=1 
            except IndexError:
                pass
            continue
print(f, " done")
a+=1
print("start: ", datetime.datetime.now())
with open(path2+"contract_net_address_hash2019_full.csv", "w", newline ='') as hfile:
    hasher = csv.writer(hfile)
    for k,v in nodes.items():
        hasher.writerow([k,v])

print(n)
print(count)
print(len(list(nodes.keys())))
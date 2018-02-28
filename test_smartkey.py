# -*- coding: utf-8 -*-
import json
from web3 import Web3, KeepAliveRPCProvider, IPCProvider, contract

import sys
import json
import codecs
import StringIO
import re
import os

def getContract(item, network, address=None):
    abi = json.loads(open('bin/' + item + '.abi').read())
    bin = open('bin/' + item + '.bin').read()
    json_data=open('build/contracts/' + item + '.json').read()
    data = json.loads(json_data)
    
    if address is None:
        address=data['networks'][network]['address']
    conf_c = web3.eth.contract(abi=abi, bytecode=bin)
    conf=conf_c(address)
    return conf

network='5'
port='8545'
web3 = Web3(KeepAliveRPCProvider(host='localhost', port=port))
address=web3.eth.coinbase
address2=web3.eth.accounts[1]

print (address, address2)
gc=getContract('SmartKey',network)
io=getContract('PublicOffering',network)
amount=1000000000000000000 #1 ETH

print ('getTokenBalanceInEth for address1', gc.call({ 'from': address2}).getBalanceInEth(address))
print ('getBalance (eth) for address1',web3.eth.getBalance(address))
print ('getBalance (eth) for address2',web3.eth.getBalance(address2))
print (io.transact({ 'from': address2, 'value': amount}).getSmartKey(address2))
print ('convertToToken', gc.call({ 'from': address2}).convertToToken(amount))
print (gc.transact({ 'from': address2, 'value': amount}).getSmartKey(address2))
#print ('getSmartKey', gc.call({ 'from': address2, 'value': amount}).getSmartKey(address2))
print ('getBalanceInEth', gc.call({ 'from': address2}).getBalanceInEth(address2))
print ('getBalance', gc.call({ 'from': address2}).getBalance(address2))
print ('getKey', gc.call({ 'from': address2 }).getKey(address2))
key=gc.call({ 'from': address2 }).getKey(address2)
kc=getContract('Key',network, key)
print ('Key Activated', kc.call({ 'from': address2}).activated(address2))
print ('Key State', kc.call({ 'from': address2}).state())
print ('getBalance (eth) for address1',web3.eth.getBalance(address))

print ('getTokenBalanceInEth for address1', gc.call({ 'from': address2}).getBalanceInEth(address))
print ('getBalance (eth) for address1',web3.eth.getBalance(address))
print ('getBalance (eth) for address2',web3.eth.getBalance(address2))
print ('getBalance (eth) for key',web3.eth.getBalance(key))
print ('getTokenBalanceInEth for key', gc.call({ 'from': address2}).getBalanceInEth(key))


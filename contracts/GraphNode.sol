pragma solidity ^0.4.18; //We have to specify what version of the compiler this code will use

import "./Catalogue.sol";

contract GraphNode is Catalogue, Key {
 
  function GraphNode(SmartKey _smartKey, address[] adminAddress) 
  public
  Catalogue(_smartKey, adminAddress)
  Key(address(this))
  {      
      
      for (uint i=0; i < adminAddress.length; i++) {
        addOwner(adminAddress[i]);
         
      } 
      addOwner(address(_smartKey));
     
  }
  
  function upsertItem(GraphNode _node, string _href)
  public
  payable
  returns (bool)
  {  
      //smartKey.addSmartKey.value(msg.value)(address(vault));  
      //bytes32 hashVal=Key(smartKey.getKey(address(vault))).getHash(_href);
      smartKey.addSmartKey.value(msg.value)(address(this));

      bytes32 hashVal=getHash(_href);
      
      if (nodeData[hashVal] == address(0)) 
      {
      
            nodeData[hashVal]=address(_node);
            items.push(address(_node));
            _node.setHref.value(msg.value)(_href);
      }
      //smartKey.addSmartKey.value(msg.value)(address(vault));
      //vault.transfer(msg.value);
      
      return true;
      
  }
  
  function getItem(string _href) 
  constant
  public
  returns (address) 
  {      
      bytes32 hashVal=getHash(_href);
      
      if (nodeData[hashVal] != address(0)) 
      {
         return nodeData[hashVal];
      }

      if (bytes(_href).length < 1)
      {
          return this;
      }
      
      return 0x0;
      
  }
    
}


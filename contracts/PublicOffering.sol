pragma solidity ^0.4.18; //We have to specify what version of the compiler this code will use


import "./crowdsale/CappedCrowdsale.sol";
import "./crowdsale/Crowdsale.sol";
import "./admin/Administered.sol";

/**
 * @title IoT Smart Keys IO
 */
contract PublicOffering is CappedCrowdsale {

  function PublicOffering(SmartKey _token, uint256 _startTime, uint256 _endTime, uint256 _rate, uint256 _cap, address[] adminAddress)
  public
  Administered(adminAddress)
  CappedCrowdsale(_cap, adminAddress)
  Crowdsale(_token, _startTime, _endTime, _rate, adminAddress)
  {
    
  }

}
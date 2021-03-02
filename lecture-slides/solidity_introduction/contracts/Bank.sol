// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.8.0;

contract Bank {
    
    address private owner;
    
    mapping (address => uint) private balances;
    
    event LogDeposit(address depositor, uint amount);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }
    
    constructor() {
        owner = msg.sender;
    }
    
    // function internal 

    function deposit() public payable returns (uint newBalance) {
        balances[msg.sender] += msg.value;
        emit LogDeposit(msg.sender, msg.value);
        return balances[msg.sender];
    }
    
    function attemptSend(address payable account, uint withdrawAmount) internal {
        bool sent = account.send(withdrawAmount);
        if ( !sent ) {
            balances[account] += withdrawAmount;
        }
    }
    
    function withdraw(uint withdrawAmount) external returns (uint newBalance) {
        if ( balances[msg.sender] >= withdrawAmount ) {
            balances[msg.sender] -= withdrawAmount;
            attemptSend(msg.sender, withdrawAmount);
        }
        
        return balances[msg.sender];
    }
    
    function balance() public view returns (uint) {
        return balances[msg.sender];
    }
    
    function balance(address account) public view onlyOwner returns (uint) {
        return balances[account];
    }
    
    fallback () external {
        revert();
    }
}
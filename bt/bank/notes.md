Blockchain & Solidity Viva Questions for Bank Account Contract
What does this smart contract implement?
It implements a simple Bank Account system on Ethereum, allowing users to create accounts, deposit and withdraw Ether, and check their balance.

How does the contract track individual user balances?
It uses a mapping from address to uint256 to store balances for each user address.

What is the purpose of the isUser mapping?
To prevent duplicate account creation and restrict deposit/withdrawal operations only to existing users.

Explain the createAccount function.
It creates a new user account with initial Ether deposit (msg.value), marks the user as active, updates the balance, and emits an event.

How does the deposit function work?
Allows an existing user to add Ether to their balance, checks that deposit amount is greater than zero, updates balance, and emits an event.

Explain the withdraw function and what safety checks it includes.
Allows withdrawal upto user’s balance. Checks user exists, balance is sufficient, then sends Ether back to user and updates mapping. Emits an event.

What is the difference between receive() and fallback() functions here?

receive is triggered when plain Ether is sent with empty calldata.

fallback is triggered when the call data does not match any function signature or if Ether sent with non-empty calldata.

How can you observe gas usage and transaction fees?
Using Remix IDE’s transaction logs and gas reports, or MetaMask transaction details when deployed on a testnet.

What security considerations apply to this contract?

Reentrancy protection is not implemented (critical for withdraw functions).

Only account holders can deposit/withdraw through the public functions.

Use of call instead of transfer might be considered modern best practice for sending Ether.

What are Solidity events and why are they used?
Events are logs emitted on state changes; useful for off-chain apps to listen and react. They also reduce on-chain storage requirements.


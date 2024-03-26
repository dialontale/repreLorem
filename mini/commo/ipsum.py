>>> from web3 import Web3, HTTPProvider
>>> w3 = Web3(HTTPProvider('http://localhost:8545'))
>>> contract = w3.eth.contract(address='0x1234567890123456789012345678901234567890', abi=[{"constant": False, "inputs": [{"name": "_value", "type": "uint256"}], "name": "set", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"}, {"constant": True, "inputs": [], "name": "get", "outputs": [{"name": "", "type": "uint256"}], "payable": False, "stateMutability": "view", "type": "function"}])
>>> tx_hash = contract.functions.set(100).transact()
>>> receipt = w3.eth.get_transaction_receipt(tx_hash)
>>> receipt.call_data.text
'0x0000000000000000000000000000000000000000000000000000000000000064'

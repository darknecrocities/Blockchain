# Let's create the README file in your working directory

readme_content = """
📦 Local Blockchain Storage App

---

🚀 Overview

This project is a local blockchain app that lets you store and retrieve a number on a simulated Ethereum blockchain running locally on your machine.

- Uses Ganache to simulate Ethereum blockchain (no real ETH, no internet required)
- Deploys a simple Solidity smart contract
- Provides a friendly Streamlit UI for interaction
- Communicates via Web3.py Python library

---

🛠️ Requirements

Requirement          | Description                                  | Purpose
---------------------|----------------------------------------------|----------------------------------------------
🐍 Python 3.7+       | Programming language                          | Run Streamlit and Web3.py
⚙️ Ganache GUI       | Local Ethereum blockchain simulator          | Test blockchain contracts locally
📜 Solidity compiler | Remix IDE (https://remix.ethereum.org)       | Write, compile & deploy contracts
📦 Streamlit         | Python web framework                          | Build interactive frontend
🔗 Web3.py           | Python Ethereum library                       | Connect and interact with blockchain

---

# ⚙️ Setup Guide

# 1. Install Python & Pip

Download from https://www.python.org/downloads/windows/  
Check install:

    python --version
    pip --version

# 2. Install dependencies

    pip install streamlit web3

# 3. Install & run Ganache

Download Ganache GUI: https://trufflesuite.com/ganache/  
Open Ganache — it will start a local blockchain at http://127.0.0.1:7545

# 4. Write & deploy the smart contract

Use Remix IDE: https://remix.ethereum.org/  
Paste contract code below, compile, connect Remix to Ganache, and deploy:

    // SPDX-License-Identifier: MIT
    pragma solidity ^0.8.0;

    contract Storage {
        uint256 number;

        function set(uint256 _num) public {
            number = _num;
        }

        function get() public view returns (uint256) {
            return number;
        }
    }

Copy the contract address and ABI after deployment.

# 5. Save ABI file

Create abi.json in your project folder and paste the contract ABI JSON from Remix.

# 6. Create app.py for Streamlit UI

Use this sample code:

    import streamlit as st
    from web3 import Web3
    import json

    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))

    with open("abi.json") as f:
        abi = json.load(f)

    contract_address = "PASTE_YOUR_CONTRACT_ADDRESS_HERE"
    contract = web3.eth.contract(address=contract_address, abi=abi)
    account = web3.eth.accounts[0]

    st.title("📦 Local Blockchain Storage")

    value = st.number_input("Enter a number to store:", value=0)

    if st.button("Store on Blockchain"):
        tx_hash = contract.functions.set(int(value)).transact({'from': account})
        receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        st.success(f"Stored successfully! TX Hash: {tx_hash.hex()}")

    if st.button("Retrieve from Blockchain"):
        result = contract.functions.get().call()
        st.info(f"Stored Value: {result}")

# 7. Run the app

    streamlit run app.py

Open browser at http://localhost:8501

---

# 🛠 Troubleshooting

- Connection failed? Make sure Ganache is running at http://127.0.0.1:7545
- BadFunctionCallOutput error? Verify contract address and ABI match your deployed contract
- ImportError for Web3? Rename/delete any web3.py file in your project folder to avoid naming conflicts

---

# 🎉 Enjoy your local blockchain app!

Build and test smart contracts easily with no gas fees, no internet, and full control over your environment.

---

Made with ❤️ by [Your Name]
"""

# Save file in current directory
with open("/mnt/data/README_Local_Blockchain_App.txt", "w") as file:
    file.write(readme_content)

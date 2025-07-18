import streamlit as st
from web3 import Web3
import json

# Connect to local Ganache blockchain
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Load contract
with open("abi.json") as f:
    abi = json.load(f)

# Replace with your actual contract address from Remix
contract_address = "YourContractAddres5"
contract = web3.eth.contract(address=contract_address, abi=abi)

# Use the first account from Ganache
account = web3.eth.accounts[0]

# UI
st.title("📦 Local Blockchain Storage")
st.markdown("Fully offline & local blockchain app using Ganache + Streamlit")

value = st.number_input("Enter a number to store:", value=0)

if st.button("Store on Blockchain"):
    tx_hash = contract.functions.set(int(value)).transact({'from': account})
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    st.success(f"Stored successfully! TX Hash: {tx_hash.hex()}")

if st.button("Retrieve from Blockchain"):
    result = contract.functions.get().call()
    st.info(f"Stored Value: {result}")

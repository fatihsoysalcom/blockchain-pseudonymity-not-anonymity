import hashlib
import os
import datetime
import json

def generate_pseudonymous_address():
    """
    Simulates generating a pseudonymous blockchain address.
    In real crypto, this would be derived from a public key.
    Here, we use a hash of random bytes to represent a unique,
    non-identifiable string.
    """
    random_bytes = os.urandom(32)
    return hashlib.sha256(random_bytes).hexdigest()

def create_transaction(sender_address, receiver_address, amount, timestamp):
    """
    Simulates a blockchain transaction.
    Transactions are public records linking pseudonymous addresses.
    """
    tx_id = hashlib.sha256(f"{sender_address}{receiver_address}{amount}{timestamp}".encode()).hexdigest()
    return {
        "transaction_id": tx_id,
        "sender": sender_address,
        "receiver": receiver_address,
        "amount": amount,
        "timestamp": timestamp.isoformat()
    }

def print_address_transactions(address, blockchain):
    """
    Filters and prints all transactions associated with a given address.
    This demonstrates the linkability aspect of pseudonymous systems.
    """
    print(f"\n--- Transactions for Address: {address[:16]}... ---")
    found_transactions = False
    for tx in blockchain:
        if tx["sender"] == address or tx["receiver"] == address:
            print(f"  ID: {tx['transaction_id'][:8]}...")
            print(f"  From: {tx['sender'][:8]}... To: {tx['receiver'][:8]}...")
            print(f"  Amount: {tx['amount']} units, Time: {tx['timestamp']}")
            print("-" * 20)
            found_transactions = True
    if not found_transactions:
        print("  No transactions found for this address.")
    print("------------------------------------------")

# --- Main simulation ---
if __name__ == "__main__":
    print("Kripto İşlemleri: Gerçekten Anonim mi, Yoksa Sadece Takma Adlı mı?")
    print("Simulating Pseudonymity vs. Anonymity in Blockchain Transactions\n")

    # 1. Generate a pseudonymous address for our user
    my_address = generate_pseudonymous_address()
    print(f"Generated a new pseudonymous address: {my_address[:16]}...") # Display first 16 chars for brevity
    # This address is a pseudonym. It doesn't directly reveal my real-world identity.

    # 2. Generate some other addresses for simulation
    other_address_1 = generate_pseudonymous_address()
    other_address_2 = generate_pseudonymous_address()
    exchange_address = generate_pseudonymous_address() # Could represent an exchange or a service

    # 3. Simulate a blockchain (a list of transactions)
    blockchain = []

    print("\nSimulating transactions on a public ledger...")

    # Transaction 1: My address sends funds
    tx1 = create_transaction(my_address, other_address_1, 10.5, datetime.datetime.now() - datetime.timedelta(days=5))
    blockchain.append(tx1)
    print(f"  - Transaction 1 created: {tx1['transaction_id'][:8]}... (from my_address)")

    # Transaction 2: My address receives funds
    tx2 = create_transaction(other_address_2, my_address, 5.0, datetime.datetime.now() - datetime.timedelta(days=3))
    blockchain.append(tx2)
    print(f"  - Transaction 2 created: {tx2['transaction_id'][:8]}... (to my_address)")

    # Transaction 3: My address sends more funds, possibly to an exchange
    tx3 = create_transaction(my_address, exchange_address, 2.0, datetime.datetime.now() - datetime.timedelta(days=1))
    blockchain.append(tx3)
    print(f"  - Transaction 3 created: {tx3['transaction_id'][:8]}... (from my_address)")

    # Transaction 4: Another unrelated transaction
    tx4 = create_transaction(other_address_1, other_address_2, 1.0, datetime.datetime.now() - datetime.timedelta(days=2))
    blockchain.append(tx4)
    print(f"  - Transaction 4 created: {tx4['transaction_id'][:8]}... (unrelated to my_address)")

    # 4. Demonstrate linkability: All transactions for 'my_address' are publicly visible
    # This is the core concept of pseudonymity in blockchain:
    # The address is a pseudonym, but all activities linked to it are public and traceable.
    # Over time, patterns, amounts, timings, and interactions with known entities (like exchanges)
    # can help de-anonymize the real-world identity behind the pseudonym.
    print_address_transactions(my_address, blockchain)

    print("\n--- Summary ---")
    print("The address is a pseudonym, not your real name.")
    print("However, all transactions involving this pseudonym are public and linked.")
    print("This 'transaction history' can potentially be used to infer real-world identity")
    print("if the pseudonym is ever linked to an off-chain identity (e.g., KYC at an exchange).")
    print("True anonymity would mean no linkability between transactions, or no way to trace them back to an individual.")
    print("Blockchain's default state is pseudonymous, not anonymous.")

 🩺 Electronic Health Records using Blockchain
This project demonstrates a secure system for storing, encrypting, and verifying patient medical data using AES encryption and blockchain technology.

 🔐 Objective
To ensure:
- Confidentiality of patient data using AES encryption.
- Integrity of medical records using SHA-256 hashing and blockchain smart contracts.
- Tamper detection using on-chain verification.

 🚀 Project Highlights
- ✅ Encrypted patient data using AES-256
- ✅ Generated SHA-256 hashes for tamper-proof tracking
- ✅ Deployed a Solidity smart contract on a simulated blockchain (Remix IDE)
- ✅ Verified data integrity using on-chain hash matching

 🧩 Architecture Overview
1. 🧾 Data Collection: Patient info is entered through a Python CLI or UI.
2. 🔐 AES Encryption: Sensitive data (e.g. diagnosis, test results) is encrypted before storage.
3. 🧬 SHA-256 Hashing: A fingerprint of the encrypted data is generated.
4. ⛓ Blockchain: Hash is stored on-chain via a smart contract.
5. 🧪 Verification: Current hash is compared with on-chain hash to detect tampering.

 🛠 Tech Stack

| Component       | Technology           |
|-----------------|------------------    |
| Language        | Python, Solidity     |
| Encryption      | AES (Crypto.Cipher)  |
| Hashing         | SHA-256 (hashlib)    |
| Blockchain      | Remix IDE (JS VM)    |
| Database        | SQLite (patients.db) |
| UI              | Flask                |

 📂 Project Structure
EHR-Blockchain/
│
├── 📁 blockchain/
│   └── smart_contract.sol         # Solidity smart contract (Remix)
│
├── 📁 database/
│   └── patients.db                # Encrypted SQLite database
│
├── 📁 encryption/
│   ├── encryption.py              # AES encryption logic
│   └── decryption.py              # AES decryption logic
│
├── 📁 scripts/
│   ├── insert_patient.py          # Insert encrypted data into DB
│   ├── view_patients.py           # Decrypt and view records
│   └── hash_all_records.py        # Generate SHA-256 hashes

 🔍 Smart Contract Overview
solidity
contract HealthRecordHashStorage {
    mapping(uint => bytes32) public recordHashes;
    uint public recordCount;

  function storeRecordHash(bytes32 _hash) public { ... }
  function verifyRecordHash(uint recordId, bytes32 hashToVerify) public view returns (bool) { ... }
}

🔐 Stores a hash of each patient record

✅ Allows later verification for tampering


✅ How to Use

1. Run insert_patient.py to store encrypted patient data.
2. Run hash_all_records.py to generate hashes.
3. Copy each hash and store it using Remix → storeRecordHash().
4. Later, use verifyRecordHash(recordId, hash) in Remix to verify data integrity.
or
Directly run the app.py which runs in the local host and displays the ui page for entering and generating the hashes.

📚 Learnings
How blockchain ensures transparency and immutability
Importance of hybrid storage (off-chain for data, on-chain for proof)
Practical use of encryption and hashing for medical privacy

🧪 Future Enhancements
Integration with Ganache + MetaMask for real blockchain simulation
Upload of medical reports (images/PDFs)
Role-based access control (doctors/patients)

📜 License
MIT License — feel free to use, fork, and learn from this project!

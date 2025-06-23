contract HealthRecordHashStorage {
    mapping(uint => bytes32) public recordHashes;
    uint public recordCount;

    function storeRecordHash(bytes32 _hash) public { ... }
    function verifyRecordHash(uint recordId, bytes32 hashToVerify) public view returns (bool) { ... }
}

🔐 Stores a hash of each patient record

✅ Allows later verification for tampering

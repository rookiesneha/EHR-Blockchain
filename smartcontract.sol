pragma solidity ^0.8.0;

contract HealthRecordHashStorage {
    mapping(uint => bytes32) public recordHashes;
    uint public recordCount;

    event RecordStored(uint indexed recordId, bytes32 hash);

    function storeRecordHash(bytes32 _hash) public {
        recordHashes[recordCount] = _hash;
        emit RecordStored(recordCount, _hash);
        recordCount++;
    }

    function verifyRecordHash(uint recordId, bytes32 hashToVerify) public view returns (bool) {
        return recordHashes[recordId] == hashToVerify;
    }
}

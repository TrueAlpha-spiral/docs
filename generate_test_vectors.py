import json
import hashlib
import hmac
import time

def get_canonical_json(data):
    # Sort keys to approximate canonical json for testing purposes
    return json.dumps(data, separators=(',', ':'), sort_keys=True).encode('utf-8')

# Mock data
session_key = b"super_secret_session_key_for_hmac"
channel_key = b"super_secret_channel_key_for_hmac"
parent_hash = "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef"
candidate_hash = "0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

payload_data = {"user_action": "commit_code", "file": "src/main.rs"}
payload_bytes = get_canonical_json(payload_data)

# Payload digest binding
digest_input = parent_hash.encode('utf-8') + b'\x00' + payload_bytes
payload_digest = hmac.new(session_key, hashlib.sha256(digest_input).digest(), hashlib.sha256).hexdigest()

# VERIFY_REQUEST
verify_request = {
    "nonce": 302,
    "parent_state_hash": parent_hash,
    "candidate_state_hash": candidate_hash,
    "payload_digest": payload_digest,
    "proof_ref": "ipfs:QmTestRef",
    "timestamp": 1710000000,
    "metadata": {"source": "executor", "priority": 1}
}

canonical_msg = get_canonical_json(verify_request)
hmac_sig = hmac.new(channel_key, canonical_msg, hashlib.sha256).hexdigest()

print("Payload Canonical JSON:", payload_bytes.decode('utf-8'))
print("Payload Digest:", payload_digest)
print("Canonical Request JSON:", canonical_msg.decode('utf-8'))
print("HMAC Signature:", hmac_sig)
